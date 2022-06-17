from Util.ChronoMeter import ChronoMeter
from Util.ParamGenerator import ParamGenerator


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

    for i in range(20):

        lambda_param = generator.get_param_lambda(number_param)
        relax_model = fl.get_lagragian_relax_model(lambda_param)

        chrono.start_chrono()
        relax_model.optimize()
        chrono.stop_chrono()

        solutions.append(relax_model.ObjVal)
        times.append(chrono.get_execution_time())

    solution_optimal = max(solutions)
    pos_max = solutions.index(solution_optimal)
    execution_time = times[pos_max]

    return solution_optimal, execution_time

def get_lb_lagrange_CFL(fl, number_param):
    chrono = ChronoMeter()
    generator = ParamGenerator(12345, 5)
    solutions = []
    times = []

    for i in range(20):
        lambda_param = generator.get_param_lambda(number_param)
        relax_model = fl.get_lagragian_relax_model(lambda_param)

        chrono.start_chrono()
        relax_model.optimize()
        chrono.stop_chrono()

        solutions.append(relax_model.ObjVal)
        times.append(chrono.get_execution_time())

    solution_optimal = max(solutions)
    pos_max = solutions.index(solution_optimal)
    execution_time = times[pos_max]

    return solution_optimal, execution_time


def get_ascent_dual_UFL(fl):
    chrono = ChronoMeter()
    w, z, c, f = fl.get_param_dual()
    delta = []
    z_final = []

    chrono.start_chrono()

    #Inizializzo zv al minimo di cuv scorrendo tutte le u
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

    sum_w = 0
    for k in range(len(w)):
        sum_w = sum_w + sum(w[k])

    #calcolo deltauv
    for u in range(len(c)):
        temp = []
        for v in range(len(c[0])):
            temp.append(f[v] - (sum_w - w[u][v]))
        delta.append(temp)

    #trovo valori finali di zv come il minimo z[v] + delta[u][v] scorrendo le u
    for v in range(len(c[0])):
        temp = []
        for u in range(len(c)):
            temp.append(z[v] + delta[u][v])

        z_final.append(min(temp))

    chrono.stop_chrono()

    solution_optimal = sum(z_final)
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
        temp_l = []
        for u in range(len(c)):
            temp.append(c[u][v] + delta[u][v])
            temp_l.append(c[u][v] + f[u])

        min_value = min(temp)
        min_pos = temp.index(min_value)
        l_final.append(temp_l[min_pos])

    chrono.stop_chrono()

    solution_optimal = sum(l_final)
    execution_time = chrono.get_execution_time()

    return solution_optimal, execution_time

