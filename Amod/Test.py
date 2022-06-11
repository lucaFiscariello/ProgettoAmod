import unittest

from Solver import Solver
from Model.ModelCFL import ModelCFL
from Model.ModelUFL import ModelUFL
from Solver.ParamGenerator import ParamGenerator


class MyTestCase(unittest.TestCase):
    def test_UFL(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(5000, 20)
        ModelUFL(fixedCosts, transCosts)

    def test_CFL(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(5000, 20)
        demands = generator.get_client_demand(20,4)
        capacity = generator.get_facility_capacity(200,5)

        ModelCFL(fixedCosts,transCosts,demands,capacity)

    def test_SolverCFL(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(5000, 20)
        demands = generator.get_client_demand(20,4)
        capacity = generator.get_facility_capacity(200,5)

        model = ModelCFL(fixedCosts,transCosts,demands,capacity)
        print(Solver.get_optimal(model))
        print(Solver.get_lb_linear(model))

    def test_UFL_lagrange(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(5000, 20)
        lambda_moltiplicator = generator.get_param_lambda(20)
        model = ModelUFL(fixedCosts, transCosts)

        print(Solver.get_optimal(model))
        print(Solver.get_lb_linear(model))
        print(Solver.get_lb_lagrange_UFL(model, lambda_moltiplicator))


    def test_UFL_dual(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(5000, 20)
        model = ModelUFL(fixedCosts, transCosts)

        print(Solver.get_ascent_dual_UFL(model))
        print(Solver.get_optimal(model))

    def test_CFL_lagrange(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(5000, 20)
        demands = generator.get_client_demand(20,4)
        capacity = generator.get_facility_capacity(200,5)

        lambda_moltiplicator = generator.get_param_lambda(5)

        model = ModelCFL(fixedCosts,transCosts,demands,capacity)
        print(Solver.get_optimal(model))
        print(Solver.get_lb_linear(model))
        print(Solver.get_lb_lagrange_UFL(model,lambda_moltiplicator))

    def test_CFL_dual(self):
        generator = ParamGenerator(1234, 5)
        fixedCosts = generator.get_setup_cost(20000, 5)
        transCosts = generator.get_allocation_cost(1000, 20)
        demands = generator.get_client_demand(150,4)
        capacity = generator.get_facility_capacity(200,5)
        lambda_moltiplicator = generator.get_param_lambda(5)

        model = ModelCFL(fixedCosts, transCosts, demands, capacity)
        print(Solver.get_ascent_dual_CFL(model))
        print(Solver.get_optimal(model))
        print(Solver.get_lb_lagrange_CFL(model,lambda_moltiplicator))
        print(Solver.get_lb_linear(model))
        
if __name__ == '__main__':
    unittest.main()
