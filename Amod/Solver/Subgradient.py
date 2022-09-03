import numpy as np

from Amod.Util.Counter import Counter
from Amod.Util.ParamGenerator import ParamGenerator


def get_lambda_moltiplicator(model):
    generator = ParamGenerator(12345, 5)
    counter = Counter()
    lambda_vector = generator.get_param_lambda(model.facility_number)

    B = model.get_feasible_solution()
    b = model.get_b_lagrange()
    a = model.get_a_lagrange()
    k = 10

    loop = True

    while loop:
        iterative_model = model.get_lagragian_relax_model(lambda_vector)
        iterative_model.optimize()
        x = iterative_model.getAttr("x")
        l = iterative_model.ObjVal

        s_h = b - np.dot(a, x)

        loop = check(s_h, l, counter, k)
        if not loop:
            return lambda_vector

        theta_h = (B - l) / (np.linalg.norm(s_h)) ** 2

        s_h = normalize(s_h, lambda_vector)
        lambda_vector = lambda_vector + ((theta_h / np.linalg.norm(s_h)) * s_h)


def normalize(s_h, lambda_vector):
    len_sh = len(s_h)
    len_lb = len(lambda_vector)

    if len_sh > len_lb:
        s_h_return = s_h[0:len_lb]
    else:
        s_h_return = [s_h[j] for j in range(len_sh)]
        for i in range(len_lb - len_sh):
            s_h_return.append(0.0)

    return np.array(s_h_return)


def check(s_h, l, counter, k):
    condition_sh = np.sum(s_h) == 0
    condition_l = counter.get_no_improve(l) >= k

    return condition_sh or condition_l
