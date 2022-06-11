import gurobipy as gp
from gurobipy import GRB


class ModelUFL:
    def __init__(self, setup_costs, allocation_costs):

        self.setup_costs = setup_costs
        self.allocation_costs = allocation_costs
        self.facility_number = len(setup_costs)
        self.client_number = int(len(allocation_costs)/self.facility_number)

        # Modello
        m = gp.Model("facility")
        m.ModelSense = GRB.MINIMIZE
        m.Params.Method = 2

        facility = range(self.facility_number)
        clients = range(self.client_number)

        # Variabile decisionale: x[u] == 1 se centro u è attivo.
        x = m.addVars(facility, vtype=GRB.BINARY, obj=setup_costs, name="X")

        # Variabile decisionale : y[u][v] == 1 se centro u serve cliente v
        y = m.addVars(facility, clients, vtype=GRB.BINARY, obj=allocation_costs, name="Y")

        # Vincoli sul soddisfacimento della domanda dei clienti
        # Sommatoria su u (yuv) == 1
        m.addConstrs((y.sum('*', v) == 1 for v in clients), "Demand")

        # Vincoli che legano le variabili di xu e yuv
        # yuv<=xu
        m.addConstrs((x[u]-y[u, v] >= 0 for u in facility for v in clients), "Continuity")

        m.write('Formulation/facilityUFL.lp')
        self.model = m

    def get_model(self):
        return self.model

    def get_linear_relax_model(self):
        return self.model.relax()

    def get_lagragian_relax_model(self, lambda_vector):
        # Modello
        m_lgr = gp.Model("facility relax lagrangian")
        m_lgr.ModelSense = GRB.MINIMIZE
        m_lgr.Params.Method = 2

        facility = range(self.facility_number)
        clients = range(self.client_number)

        x_moltiplicator = [self.setup_costs[u] - sum(lambda_vector) for u in facility]
        y_moltiplicator = [self.allocation_costs[(self.client_number+1)*v + u] + lambda_vector[(self.client_number+1)*v + u] for v in clients for u in facility]

        # Variabile decisionale: x[u] == 1 se centro u è attivo.
        x = m_lgr.addVars(facility, vtype=GRB.BINARY, obj=x_moltiplicator, name="X")

        # Variabile decisionale : y[u][v] == 1 se centro u serve cliente v
        y = m_lgr.addVars(facility, clients, vtype=GRB.BINARY, obj=y_moltiplicator, name="Y")

        # Vincoli sul soddisfacimento della domanda dei clienti
        # Sommatoria su u (yuv) == 1
        m_lgr.addConstrs((y.sum('*', v )== 1 for v in clients), "Demand")

        m_lgr.write('Formulation/facilityUFL_lagrange.lp')
        return m_lgr

    def get_param_dual(self):
        w = []
        z = []
        c = []
        f = self.setup_costs

        tmp = []
        for i in range(len(self.allocation_costs)):

            if i % self.client_number == 0 and not i == 0:
                c.append(tmp)
                tmp = []

            tmp.append(self.allocation_costs[i])

        c.append(tmp)

        return w, z, c, f






