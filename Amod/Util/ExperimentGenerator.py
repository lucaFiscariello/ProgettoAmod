from Amod.Model.ModelCFL import ModelCFL
from Amod.Util.ParamGenerator import ParamGenerator
from Amod.Solver import Solver
import pandas as pd


class ExperimentGeneratorCFL:
    def __init__(self, run_number, seed, number_client, number_facility, mean_trans,
                 mean_setup, var_trans, var_setup,mean_capacity,mean_demand,var_capacity,var_demand):

        self.run_number = run_number
        self.seed = seed

        self.number_client = number_client
        self.number_facility = number_facility

        self.mean_trans = mean_trans
        self.mean_setup = mean_setup
        self.var_trans = var_trans
        self.var_setup = var_setup

        self.mean_capacity = mean_capacity
        self.mean_demand = mean_demand
        self.var_capacity = var_capacity
        self.var_demand = var_demand

        self.stream = 5

    def generate_cfl(self):
        generator = ParamGenerator(self.seed, self.stream)

        solutions_opt = []
        solutions_linear = []
        solutions_lagrange = []
        solutions_asc = []
        times_opt = []
        times_linear = []
        times_lagrange = []
        times_asc = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost_normal(self.mean_setup,self.var_setup, self.number_facility)
            trans_costs = generator.get_allocation_cost_normal(self.mean_trans, self.var_trans, self.number_client*self.number_facility)
            demands = generator.get_client_demand_normal(self.mean_demand, self.var_demand, self.number_client)
            capacity = generator.get_facility_capacity_normal(self.mean_capacity, self.var_capacity, self.number_facility)
            model = ModelCFL(fixed_costs, trans_costs, demands, capacity)

            solution_opt, time_opt = Solver.get_optimal(model)
            solution_linear, time_linear = Solver.get_lb_linear(model)
            solution_asc, time_asc = Solver.get_ascent_dual_CFL(model)
            solution_lagrange, time_lagrange = Solver.get_lb_lagrange_CFL(model)

            solutions_opt.append(solution_opt)
            solutions_linear.append(solution_linear)
            solutions_lagrange.append(solution_lagrange)
            solutions_asc.append(solution_asc)

            times_opt.append(time_opt)
            times_linear.append(time_linear)
            times_lagrange.append(time_lagrange)
            times_asc.append(time_asc)

        df = pd.DataFrame(list(zip(solutions_opt,solutions_linear,solutions_lagrange,solutions_asc,times_opt,times_linear,times_lagrange,times_asc)),
                          columns=['solutions opt', 'solutions_linear','solutions_lagrange','solutions_asc','times_opt','times_linear','times_lagrange','times_asc'])

        return df
