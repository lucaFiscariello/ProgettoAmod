import gurobipy as gp
from gurobipy import GRB


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

    def get_lagragian_relax_model(self, lambda_vector):
        # Modello
        m_lgr = gp.Model("facility relax lagrangian cfl")
        m_lgr.ModelSense = GRB.MINIMIZE
        m_lgr.Params.Method = 2

        facility = range(self.facility_number)
        clients = range(self.client_number)

        x_moltiplicator = [self.setup_costs[u] - self.capacity[u]*lambda_vector[u] for u in facility]
        y_moltiplicator = [self.allocation_costs[(self.client_number+1)*v + u] + lambda_vector[u]+self.demands[v] for v in clients for u in facility]

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





