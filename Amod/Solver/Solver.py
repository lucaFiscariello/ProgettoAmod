from Amod.Util.ChronoMeter import ChronoMeter


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

def get_lb_lagrange_CFL(fl):
    chrono = ChronoMeter()

    chrono.start_chrono()
    relax_model = fl.get_lagragian_sub_relax_model()
    relax_model.optimize()
    chrono.stop_chrono()

    solution_optimal = relax_model.ObjVal
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


