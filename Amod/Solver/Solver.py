from Amod.Util.ChronoMeter import ChronoMeter
from Amod.Util.ParamGenerator import ParamGenerator


def get_optimal(fl):
    chrono = ChronoMeter()
    model = fl.get_model()

    chrono.start_chrono()
    model.optimize()
    chrono.stop_chrono()

    solution_optimal = model.ObjVal
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time

def get_lb_linear(fl):
    chrono = ChronoMeter()
    relax_model = fl.get_linear_relax_model()

    chrono.start_chrono()
    relax_model.optimize()
    chrono.stop_chrono()

    solution_optimal = relax_model.ObjVal
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time

def get_lb_lagrange_UFL(fl, number_param):
    chrono = ChronoMeter()
    generator = ParamGenerator(12345, 5)
    solutions = []
    times = []

    chrono.start_chrono()
    for i in range(20):

        lambda_param = generator.get_param_lambda(number_param)
        relax_model = fl.get_lagragian_relax_model(lambda_param)

        relax_model.optimize()

        solutions.append(relax_model.ObjVal)
        times.append(chrono.get_execution_time())

    chrono.stop_chrono()

    solution_optimal = max(solutions)
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time

def get_lb_lagrange_CFL(fl, number_param):
    chrono = ChronoMeter()
    generator = ParamGenerator(12345, 5)
    solutions = []
    times = []

    chrono.start_chrono()
    for i in range(20):
        lambda_param = generator.get_param_lambda(number_param)
        relax_model = fl.get_lagragian_relax_model(lambda_param)

        relax_model.optimize()

        solutions.append(relax_model.ObjVal)
        times.append(chrono.get_execution_time())

    chrono.stop_chrono()
    solution_optimal = max(solutions)
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time


def get_ascent_dual_UFL(fl):
    chrono = ChronoMeter()
    w, z, c, f = fl.get_param_dual()

    chrono.start_chrono()

    # Inizializzo zv al minimo di cuv scorrendo tutte le u
    for v in range(len(c[0])):
        temp = []
        for u in range(len(c)):
            temp.append(c[u][v])

        z.append(min(temp))

    #calcolo wuv=max(0,zv - cuv)
    for u in range(len(c)):
        temp = []
        for v in range(len(c[0])):
            temp.append(max(0, z[v]-c[u][v]))

        w.append(temp)

    # trovo valori finali di zv come il minimo z[v] + delta[u][v] scorrendo le u
    for v in range(len(c[0])):
        temp = []
        for u in range(len(c)):
            temp.append(c[u][v] + f[u] - sum([max(0,z[v]-w[u][i]) for i in range(len(c[0]))])+max(0,z[v]-c[u][v]))

        z[v]=min(temp)

    chrono.stop_chrono()

    solution_optimal = sum(z)
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time

def get_ascent_dual_CFL(fl):
    chrono = ChronoMeter()
    c, f, k, d = fl.get_param_dual()
    delta = []
    l_final = []

    chrono.start_chrono()

    for u in range(len(c)):
        temp = []
        for v in range(len(c[0])):
            temp.append(int((f[u]*d[v])/k[u]))
        delta.append(temp)

    #trovo valori finali di lv come c[u][v] + f[u] in corrispondenza del minimo c[u][v] + delta[u][v] scorrendo le u
    for v in range(len(c[0])):
        temp = []
        for u in range(len(c)):
            temp.append(c[u][v] + delta[u][v])

        l_final.append(min(temp))

    chrono.stop_chrono()

    solution_optimal = sum(l_final)
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time


