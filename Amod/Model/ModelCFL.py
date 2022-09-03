import gurobipy as gp
from gurobipy import GRB
from Amod.Solver import Subgradient


class ModelCFL:
    def __init__(self, setup_costs, allocation_costs , demands , capacity):

        self.setup_costs = setup_costs
        self.allocation_costs = allocation_costs
        self.demands = demands
        self.capacity = capacity
        self.client_number = len(demands)
        self.facility_number = len(setup_costs)

        # Modello
        m = gp.Model("facility")
        m.ModelSense = GRB.MINIMIZE
        m.Params.Method = 2

        clients = range(self.client_number)
        facility = range(self.facility_number)

        # Variabile decisionale: x[u] == 1 centro u è attivo.
        x = m.addVars(facility, vtype=GRB.BINARY, obj=setup_costs, name="X")

        # Variabile decisionale : y[u][v] rappresenta la percentuale della domanda di v che il centro u serve al cliente v
        y = m.addVars(facility, clients, vtype=GRB.BINARY,  obj=allocation_costs, name="y")

        # Vincoli sulla capacità
        # Sommatoria su v (yuv)*dv <= ku*xu
        m.addConstrs((sum(y[u, v]*demands[v] for v in clients) <= capacity[u] * x[u] for u in facility), "Capacity")

        # Vincoli sul soddisfacimento della domanda dei clienti
        # Sommatoria su u (yuv) == 1
        m.addConstrs((y.sum('*', v) == 1 for v in clients), "Demand")
        m.write('Formulation/facilityCFL.lp')
        self.model = m

    def get_model(self):
        return self.model

    def get_linear_relax_model(self):
        return self.model.relax()

    def get_lagragian_sub_relax_model(self):
        # Modello
        m_lgr = gp.Model("facility relax lagrangian cfl")
        m_lgr.ModelSense = GRB.MINIMIZE
        m_lgr.Params.Method = 2

        lambda_vector = Subgradient.get_lambda_moltiplicator(self)

        facility = range(self.facility_number)
        clients = range(self.client_number)
        allocation_costs = self.get_cost_matrix()

        x_moltiplicator = [self.setup_costs[u] - self.capacity[u]*lambda_vector[u] for u in facility]
        y_moltiplicator = [allocation_costs[u][v] + lambda_vector[u]*self.demands[v] for v in clients for u in facility]

        # Variabile decisionale: x[u] == 1 se centro u è attivo.
        x = m_lgr.addVars(facility, vtype=GRB.BINARY, obj=x_moltiplicator, name="X")

        # Variabile decisionale : y[u][v] == 1 se centro u serve cliente v
        y = m_lgr.addVars(facility, clients, vtype=GRB.BINARY, obj=y_moltiplicator, name="Y")

        # Vincoli sul soddisfacimento della domanda dei clienti
        # Sommatoria su u (yuv) == 1
        m_lgr.addConstrs((y.sum('*', v) == 1 for v in clients), "Demand")

        m_lgr.write('Formulation/facilityCFL_lagrange.lp')
        return m_lgr


    def get_lagragian_relax_model(self,lambda_vector):
        # Modello
        m_lgr = gp.Model("facility relax lagrangian cfl")
        m_lgr.ModelSense = GRB.MINIMIZE
        m_lgr.Params.Method = 2

        facility = range(self.facility_number)
        clients = range(self.client_number)
        allocation_cost = self.get_cost_matrix()

        x_moltiplicator = [self.setup_costs[u] - self.capacity[u]*lambda_vector[u] for u in facility]
        y_moltiplicator = [allocation_cost[u][v] + lambda_vector[u]+self.demands[v] for v in clients for u in facility]

        # Variabile decisionale: x[u] == 1 se centro u è attivo.
        x = m_lgr.addVars(facility, vtype=GRB.BINARY, obj=x_moltiplicator, name="X")

        # Variabile decisionale : y[u][v] == 1 se centro u serve cliente v
        y = m_lgr.addVars(facility, clients, vtype=GRB.BINARY, obj=y_moltiplicator, name="Y")

        # Vincoli sul soddisfacimento della domanda dei clienti
        # Sommatoria su u (yuv) == 1
        m_lgr.addConstrs((y.sum('*', v )== 1 for v in clients), "Demand")
        m_lgr.write('Formulation/facilityCFL_lagrange.lp')
        return m_lgr


    def get_param_dual(self):
        c = []
        f = self.setup_costs
        k = self.capacity
        d = self.demands

        tmp = []
        for i in range(len(self.allocation_costs)):

            if i % self.client_number == 0 and not i == 0:
                c.append(tmp)
                tmp = []

            tmp.append(self.allocation_costs[i])

        c.append(tmp)

        return c, f, k, d

    def get_a(self):
        self.model.optimize()
        return self.model.getA().toarray()

    def get_a_lagrange(self):
        self.model.optimize()
        a = self.model.getA().toarray()
        return a[0:self.client_number]

    def get_b(self):
        b = []
        for i in range(self.client_number+self.facility_number):
            if i < self.facility_number:
                b.append(0)
            else:
                b.append(1)

        return b

    def get_b_lagrange(self):
        return [1 for i in range(self.client_number)]

    def get_cost_matrix(self):
        c = []

        tmp = []
        for i in range(len(self.allocation_costs)):

            if i % self.client_number == 0 and not i == 0:
                c.append(tmp)
                tmp = []

            tmp.append(self.allocation_costs[i])

        c.append(tmp)

        return c

    def get_feasible_solution(self):
        actual_facility=0
        solution_feasible = self.allocation_costs[actual_facility]
        total_demand_facility = [0 for i in range(self.facility_number)]
        cost_matrix = self.get_cost_matrix()

        for client in range(self.client_number):
            if self.demands[client]+total_demand_facility[actual_facility] <= self.capacity[actual_facility]:
                solution_feasible = solution_feasible + cost_matrix[actual_facility][client]
                total_demand_facility[actual_facility] = total_demand_facility[actual_facility] + self.demands[client]
            else:
                actual_facility = actual_facility + 1
                solution_feasible = solution_feasible + self.allocation_costs[actual_facility]

        return solution_feasible
