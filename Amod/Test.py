import unittest
import pandas as pd

from Model.ModelCFL import ModelCFL
from Model.ModelUFL import ModelUFL
from Solver import Solver
from Util.GraphicGenerator import GraphicGenerator
from Util.ParamGenerator import ParamGenerator
from Util.TestGenerator import TestGeneratorUFL
from Util.TestGenerator import TestGeneratorCFL


class MyTestCase(unittest.TestCase):

    def test_opt_ufl(self):
        generator = TestGeneratorUFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000)

        generator.generate_opt_ufl()

    def test_linear_ufl(self):
        generator = TestGeneratorUFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000)

        generator.generate_linear_ufl()

    def test_lagrange_ufl(self):
        initial_number_client = 5
        initial_number_facility = 6

        generator = TestGeneratorUFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000)

        generator.generate_lagrange_ufl(initial_number_client*initial_number_facility)

    def test_ascent_ufl(self):
        generator = TestGeneratorUFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000)

        generator.generate_ascent_ufl()

    def test_opt_cfl(self):
        generator = TestGeneratorCFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000, initial_capacity=200, initial_demand=50)

        generator.generate_opt_cfl()

    def test_linear_cfl(self):
        generator = TestGeneratorCFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000, initial_capacity=200, initial_demand=50)

        generator.generate_linear_cfl()

    def test_lagrange_cfl(self):
        initial_number_client = 5
        initial_number_facility = 6

        generator = TestGeneratorCFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000, initial_capacity=200,
                                     initial_demand=50)

        generator.generate_lagrange_cfl(initial_number_client*initial_number_facility)

    def test_ascent_cfl(self):
        generator = TestGeneratorCFL(run_number=40, seed=12345, initial_number_client=5, initial_number_facility=6,
                                     initial_cost_f=2000000, initial_cost_t=500000, initial_capacity=200,
                                     initial_demand=50)

        generator.generate_ascent_cfl()

    def test_complex_ufl(self):
        generator = ParamGenerator(12345, 5)

        max_fixed_cost = 2000000
        max_trans_cost = 500000
        number_clients = 5
        number_facility = 6

        solutions_opt = []
        solutions_linear = []
        solutions_lgr = []
        solutions_asc = []
        times_opt = []
        times_linear = []
        times_lgr = []
        times_asc = []
        dimention = []

        while number_facility < 45:
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients * number_facility)
            model = ModelUFL(fixed_costs, trans_costs)

            solution_opt, time_opt = Solver.get_optimal(model)
            solution_linear, time_linear = Solver.get_lb_linear(model)
            solution_lgr, time_lgr = Solver.get_lb_lagrange_UFL(model, number_clients * number_facility)
            solution_asc, time_asc = Solver.get_ascent_dual_UFL(model)

            solutions_opt.append(solution_opt)
            solutions_linear.append(solution_linear)
            solutions_lgr.append(solution_lgr)
            solutions_asc.append(solution_asc)
            times_opt.append(time_opt)
            times_linear.append(time_linear)
            times_lgr.append(time_lgr)
            times_asc.append(time_asc)

            dimention.append(number_clients+number_facility)

            number_facility = number_facility + 1
            number_clients = number_clients + 1

        df = pd.DataFrame(list(zip(solutions_opt, solutions_linear, solutions_lgr, solutions_asc, times_opt, times_linear, times_lgr, times_asc , dimention)),
                          columns=['solutions opt', 'solutions linear', 'solutions lgr', 'solutions asc', 'times opt', 'times linear', 'times lgr', 'times asc', 'dimention'])
        df.to_csv("CSV/UFL/complex.csv")

    def test_complex_cfl(self):
        generator = ParamGenerator(12345, 5)

        max_fixed_cost = 2000000
        max_trans_cost = 500000
        max_demand = 100
        max_capacity = 300
        number_clients = 5
        number_facility = 6

        solutions_opt = []
        solutions_linear = []
        solutions_lgr = []
        solutions_asc = []
        times_opt = []
        times_linear = []
        times_lgr = []
        times_asc = []
        dimention = []

        while number_facility < 45:
            fixed_costs = generator.get_setup_cost(max_fixed_cost, number_facility)
            trans_costs = generator.get_allocation_cost(max_trans_cost, number_clients * number_facility)
            demands = generator.get_client_demand(max_demand, number_clients)
            capacity = generator.get_facility_capacity(max_capacity, number_facility)
            model = ModelCFL(fixed_costs, trans_costs, demands, capacity)

            solution_opt, time_opt = Solver.get_optimal(model)
            solution_linear, time_linear = Solver.get_lb_linear(model)
            solution_lgr, time_lgr = Solver.get_lb_lagrange_CFL(model, number_clients * number_facility)
            solution_asc, time_asc = Solver.get_ascent_dual_CFL(model)

            solutions_opt.append(solution_opt)
            solutions_linear.append(solution_linear)
            solutions_lgr.append(solution_lgr)
            solutions_asc.append(solution_asc)
            times_opt.append(time_opt)
            times_linear.append(time_linear)
            times_lgr.append(time_lgr)
            times_asc.append(time_asc)

            dimention.append(number_clients+number_facility)

            number_facility = number_facility + 1
            number_clients = number_clients + 1

        df = pd.DataFrame(list(zip(solutions_opt, solutions_linear, solutions_lgr, solutions_asc, times_opt, times_linear, times_lgr, times_asc , dimention)),
                          columns=['solutions opt', 'solutions linear', 'solutions lgr', 'solutions asc', 'times opt', 'times linear', 'times lgr', 'times asc', 'dimention'])
        df.to_csv("CSV/CFL/complex.csv")

    def test_imm(self):
        img_generartor = GraphicGenerator()
        img_generartor.plot_boxplot_solution_ufl()
        img_generartor.plot_boxplot_time_ufl()
        img_generartor.plot_boxplot_solution_cfl()
        img_generartor.plot_boxplot_time_cfl()
        img_generartor.plot_lineplot_solution_ufl()
        img_generartor.plot_lineplot_ascent_ufl()
        img_generartor.plot_lineplot_time_ufl()
        img_generartor.plot_error_solution_ufl()
        img_generartor.plot_lineplot_solution_cfl()
        img_generartor.plot_lineplot_ascent_cfl()
        img_generartor.plot_lineplot_time_cfl()
        img_generartor.plot_error_solution_cfl()

if __name__ == '__main__':
    unittest.main()
