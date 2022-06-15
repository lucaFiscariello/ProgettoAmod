import Solver.Solver
from Model.ModelCFL import ModelCFL
from Model.ModelUFL import ModelUFL
from Util.ParamGenerator import ParamGenerator
from Solver import Solver
import pandas as pd


class TestGeneratorUFL:
    def __init__(self, run_number, seed, initial_number_client, initial_number_facility, initial_cost_f, initial_cost_t):
        self.run_number = run_number
        self.seed = seed
        self.initial_number_client = initial_number_client
        self.initial_number_facility = initial_number_facility
        self.initial_cost_f = initial_cost_f
        self.initial_cost_t = initial_cost_t
        self.stream = 5

    def generate_opt_ufl(self):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients*number_facility)
            model = ModelUFL(fixed_costs, trans_costs)

            solution, time = Solver.get_optimal(model)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions opt', 'times opt'])
        df.to_csv("CSV/UFL/opt.csv")

    def generate_linear_ufl(self):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients*number_facility)
            model = ModelUFL(fixed_costs, trans_costs)

            solution, time = Solver.get_lb_linear(model)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions linear', 'times linear'])
        df.to_csv("CSV/UFL/linear.csv")

    def generate_lagrange_ufl(self, lambda_moltiplicator):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients*number_facility)
            model = ModelUFL(fixed_costs, trans_costs)

            solution, time = Solver.get_lb_lagrange_UFL(model, lambda_moltiplicator)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions lagrange', 'times lagrange'])
        df.to_csv("CSV/UFL/lagrange.csv")

    def generate_ascent_ufl(self):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients*number_facility)
            model = ModelUFL(fixed_costs, trans_costs)

            solution, time = Solver.get_ascent_dual_UFL(model)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions ascent', 'times ascent'])
        df.to_csv("CSV/UFL/ascent.csv")


class TestGeneratorCFL:
    def __init__(self, run_number, seed, initial_number_client, initial_number_facility, initial_cost_f,
                 initial_cost_t, initial_demand, initial_capacity):
        self.run_number = run_number
        self.seed = seed
        self.initial_number_client = initial_number_client
        self.initial_number_facility = initial_number_facility
        self.initial_cost_f = initial_cost_f
        self.initial_cost_t = initial_cost_t
        self.initial_demand = initial_demand
        self.initial_capacity = initial_capacity
        self.stream = 5

    def generate_opt_cfl(self):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        max_demand = self.initial_demand
        max_capacity = self.initial_capacity
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients * number_facility)
            demands = generator.get_client_demand(max_demand, number_clients)
            capacity = generator.get_facility_capacity(max_capacity, number_facility)
            model = ModelCFL(fixed_costs, trans_costs, demands, capacity)

            solution, time = Solver.get_optimal(model)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions opt', 'times opt'])
        df.to_csv("CSV/CFL/opt.csv")

    def generate_linear_cfl(self):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        max_demand = self.initial_demand
        max_capacity = self.initial_capacity
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients * number_facility)
            demands = generator.get_client_demand(max_demand, number_clients)
            capacity = generator.get_facility_capacity(max_capacity, number_facility)
            model = ModelCFL(fixed_costs, trans_costs, demands, capacity)

            solution, time = Solver.get_lb_linear(model)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions linear', 'times linear'])
        df.to_csv("CSV/CFL/linear.csv")

    def generate_lagrange_cfl(self, lambda_moltiplicator):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        max_demand = self.initial_demand
        max_capacity = self.initial_capacity
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients * number_facility)
            demands = generator.get_client_demand(max_demand, number_clients)
            capacity = generator.get_facility_capacity(max_capacity, number_facility)
            model = ModelCFL(fixed_costs, trans_costs, demands, capacity)

            solution, time = Solver.get_lb_lagrange_CFL(model, lambda_moltiplicator)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions lagrange', 'times lagrange'])
        df.to_csv("CSV/CFL/lagrange.csv")

    def generate_ascent_cfl(self):
        generator = ParamGenerator(self.seed, self.stream)
        max_fixed_cost = self.initial_cost_f
        max_trans_cost = self.initial_cost_t
        max_demand = self.initial_demand
        max_capacity = self.initial_capacity
        number_clients = self.initial_number_client
        number_facility = self.initial_number_facility

        solutions = []
        times = []

        for i in range(self.run_number):
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients * number_facility)
            demands = generator.get_client_demand(max_demand, number_clients)
            capacity = generator.get_facility_capacity(max_capacity, number_facility)
            model = ModelCFL(fixed_costs, trans_costs, demands, capacity)

            solution, time = Solver.get_ascent_dual_CFL(model)

            solutions.append(solution)
            times.append(time)

        df = pd.DataFrame(list(zip(solutions, times)), columns=['solutions ascent', 'times ascent'])
        df.to_csv("CSV/CFL/ascent.csv")
