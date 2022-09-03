import json
import unittest
import pandas as pd
from Model.ModelCFL import ModelCFL
from Solver import Solver
from Util.GraphicGenerator import GraphicGenerator
from Util.ParamGenerator import ParamGenerator
from Amod.Util.ExperimentGenerator import ExperimentGeneratorCFL


class MyTestCase(unittest.TestCase):

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
            solution_lgr, time_lgr = Solver.get_lb_lagrange_CFL(model)
            solution_asc, time_asc = Solver.get_ascent_dual_CFL(model)

            solutions_opt.append(solution_opt)
            solutions_linear.append(solution_linear)
            solutions_lgr.append(solution_lgr)
            solutions_asc.append(solution_asc)
            times_opt.append(time_opt)
            times_linear.append(time_linear)
            times_lgr.append(time_lgr)
            times_asc.append(time_asc)

            dimention.append(number_clients + number_facility)

            number_facility = number_facility + 1
            number_clients = number_clients + 1

        df = pd.DataFrame(list(
            zip(solutions_opt, solutions_linear, solutions_lgr, solutions_asc, times_opt, times_linear, times_lgr,
                times_asc, dimention)),
                          columns=['solutions opt', 'solutions linear', 'solutions lgr', 'solutions asc', 'times opt',
                                   'times linear', 'times lgr', 'times asc', 'dimention'])
        df.to_csv("CSV/CFL/complex.csv")

    # clienti >> centri
    # clienti == centri

    # var(capacita) alta
    # var(capacita) bassa

    # var(domanda) alta
    # var(domanda) bassa

    # trans == setup
    # trans << setup

    # rapporto media capacità/domanda basso
    # rapporto media capacità/domanda alto
    def test_variance(self):
        client_facility = ["client >> facility", "client == facility"]
        cost_trans_setup = ["trans == setup", "trans << setup"]
        var_capacity_type = ["high", "low"]
        var_demand_type = ["high", "low"]
        ratio_capacity_demand = ["high", "low"]

        file_configuration = open('Configuration.json')
        configuration = json.load(file_configuration)

        i = 0
        iterative_df = None

        for conf_cl_fc in client_facility:
            for conf_tr_st in cost_trans_setup:
                for conf_var_cap in var_capacity_type:
                    for conf_var_dem in var_demand_type:
                        for conf_ratio in ratio_capacity_demand:
                            number_client = configuration[conf_cl_fc]["number_client"]
                            number_facility = configuration[conf_cl_fc]["number_facility"]

                            mean_trans = configuration[conf_tr_st]["mean_trans"]
                            mean_setup = configuration[conf_tr_st]["mean_setup"]
                            var_trans = configuration["default_var_trans"]
                            var_setup = configuration["default_var_setup"]

                            mean_capacity = configuration["default_mean_capacity"]
                            mean_demand = configuration["default_mean_demand"]
                            var_capacity = configuration["var_capacity"][conf_var_cap]
                            var_demand = configuration["var_demand"][conf_var_dem]

                            ratio = configuration["ratio_capacity_demand"][conf_ratio]
                            mean_demand = mean_demand * ratio

                            experiment_generator = ExperimentGeneratorCFL(run_number=5, seed=12345,
                                                                          number_client=number_client,
                                                                          number_facility=number_facility,
                                                                          mean_trans=mean_trans, mean_setup=mean_setup,
                                                                          var_trans=var_trans, var_setup=var_setup,
                                                                          mean_capacity=mean_capacity,
                                                                          mean_demand=mean_demand,
                                                                          var_capacity=var_capacity,
                                                                          var_demand=var_demand
                                                                          )

                            df = experiment_generator.generate_cfl()
                            new_df = df.assign(client_facility=conf_cl_fc)
                            new_df = new_df.assign(cost_trans_setup=conf_tr_st)
                            new_df = new_df.assign(var_demand_type=conf_var_dem)
                            new_df = new_df.assign(var_capacity_type=conf_var_cap)
                            new_df = new_df.assign(ratio_capacity_demand=conf_ratio)

                            if iterative_df is None:
                                iterative_df = new_df
                            else:
                                iterative_df = iterative_df.merge(new_df, how='outer')

                            new_df.to_csv("CSV2/CFL/case{i}.csv".format(i=i))
                            i = i + 1

        iterative_df.to_csv("CSV2/CFL/total.csv")


    def test_imm(self):
        dataset_path = "CSV2/CFL/total.csv"
        dataset = pd.read_csv(dataset_path)
        img_generartor = GraphicGenerator(dataset_path)

        filter_dataset = dataset[dataset["cost_trans_setup"] == "trans == setup"]
        img_generartor.plot_boxplot_solution_cfl(filter_dataset, "box_tr_==_st")
        img_generartor.plot_boxplot_time_cfl(filter_dataset,"time_tr_==_st")

        filter_dataset = dataset[dataset["cost_trans_setup"] == "trans << setup"]
        img_generartor.plot_boxplot_solution_cfl(filter_dataset, "box_tr_minor_st")
        img_generartor.plot_boxplot_time_cfl(filter_dataset,"time_tr_minor_st")

        filter_dataset = dataset[dataset["client_facility"] == "client >> facility"]
        img_generartor.plot_boxplot_solution_cfl(filter_dataset, "box_cl_mag_fa")
        img_generartor.plot_boxplot_time_cfl(filter_dataset,"time_cl_mag_fa")

        filter_dataset = dataset[dataset["client_facility"] == "client == facility"]
        img_generartor.plot_boxplot_solution_cfl(filter_dataset, "box_cl_==_fa")
        img_generartor.plot_boxplot_time_cfl(filter_dataset,"time_cl_==_fa")

        filter_dataset = dataset[dataset["ratio_capacity_demand"] == "high"]
        img_generartor.plot_boxplot_solution_cfl(filter_dataset, "box_ratio_high")
        img_generartor.plot_boxplot_time_cfl(filter_dataset,"time_ratio_high")

        filter_dataset = dataset[dataset["ratio_capacity_demand"] == "low"]
        img_generartor.plot_boxplot_solution_cfl(filter_dataset, "box_ratio_low")
        img_generartor.plot_boxplot_time_cfl(filter_dataset,"time_ratio_low")

        img_generartor.plot_error_cfl(dataset)

        img_generartor.plot_lineplot_solution_cfl()
        img_generartor.plot_lineplot_ascent_cfl()
        img_generartor.plot_lineplot_time_cfl()
        img_generartor.plot_error_solution_cfl()


if __name__ == '__main__':
    unittest.main()
