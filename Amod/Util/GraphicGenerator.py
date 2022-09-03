import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class GraphicGenerator:
    def __init__(self,dataset_path):
        self.dataset = pd.read_csv(dataset_path)

    def plot_boxplot_solution_cfl(self,dataset,name):
        filter_dataset = dataset[['solutions opt', 'solutions_linear', 'solutions_lagrange', 'solutions_asc']]
        filter_dataset = filter_dataset.copy()
        filter_dataset.rename(
            columns={'solutions opt': 'opt', 'solutions_linear': 'linear', 'solutions_lagrange': 'lagrange',
                     'solutions_asc': 'AAD'}, inplace=True)

        fig = plt.figure(figsize=[11, 15])
        filter_dataset.boxplot(rot=45, fontsize=17)

        plt.ylabel("Costi complessivi",fontsize=20)
        plt.title("Andamento costi", fontsize=20)

        fig.savefig("Img2/CFL/{name}.png".format(name=name), format="png")

    def plot_error_cfl(self,dataset):

        error_linear = []
        error_lag = []
        error_asc = []

        error_linear_y = []
        error_lag_y = []
        error_asc_y = []

        error_best_y = []
        time_best_y = []

        client_facility = ["client >> facility", "client == facility"]
        cost_trans_setup = ["trans == setup", "trans << setup"]
        var_capacity_type = ["high", "low"]
        var_demand_type = ["high", "low"]
        ratio_capacity_demand = ["high", "low"]

        i=0

        for conf_cl_fc in client_facility:
            for conf_tr_st in cost_trans_setup:
                for conf_var_cap in var_capacity_type:
                    for conf_var_dem in var_demand_type:
                        for conf_ratio in ratio_capacity_demand:

                            filter_dataset = dataset[dataset["client_facility"] == conf_cl_fc]
                            filter_dataset = filter_dataset[filter_dataset["cost_trans_setup"] == conf_tr_st]
                            filter_dataset = filter_dataset[filter_dataset["var_capacity_type"] == conf_var_cap]
                            filter_dataset = filter_dataset[filter_dataset["var_demand_type"] == conf_var_dem]
                            filter_dataset = filter_dataset[filter_dataset["ratio_capacity_demand"] == conf_ratio]

                            column_opt = list(filter_dataset['solutions opt'])
                            mean_opt = sum(column_opt) / len(column_opt)

                            column_linear = list(filter_dataset['solutions_linear'])
                            column_linear_time = list(filter_dataset['times_linear'])
                            mean_linear = sum(column_linear) / len(column_linear)
                            mean_linear_time = sum(column_linear_time) / len(column_linear_time)

                            column_lagr = list(filter_dataset['solutions_lagrange'])
                            column_lagr_time = list(filter_dataset['times_lagrange'])
                            mean_lagr = sum(column_lagr) / len(column_lagr)
                            mean_lagr_time = sum(column_lagr_time) / len(column_lagr_time)

                            column_asc = list(filter_dataset['solutions_asc'])
                            column_asc_time = list(filter_dataset['times_asc'])
                            mean_asc = sum(column_asc) / len(column_asc)
                            mean_asc_time = sum(column_asc_time) / len(column_asc_time)

                            error_lg = abs(abs(mean_lagr)-mean_opt)/mean_opt
                            error_lag.append(error_lg)
                            error_lag_y.append("{val}-      lgr-{i}".format(i=i,val=error_lg))

                            error_ln = abs(mean_opt-mean_linear)/mean_opt
                            error_linear.append(error_ln)
                            error_linear_y.append("{val}-       lin-{i}".format(i=i,val=error_ln))

                            error_aad = abs(mean_opt-mean_asc)/mean_opt
                            error_asc.append(error_aad)
                            error_asc_y.append("{val}-      asc-{i}".format(i=i,val=error_aad))

                            error_best = min(error_aad,error_lg,error_ln)
                            if error_best == error_aad:
                                error_best_y.append("AAD")
                            elif error_best == error_lg:
                                error_best_y.append("Lagrangian")
                            else:
                                error_best_y.append("Linear")

                            time_best = min(mean_lagr_time,mean_linear_time,mean_asc_time)
                            if time_best == mean_asc_time:
                                time_best_y.append("AAD")
                            elif time_best == mean_lagr_time:
                                time_best_y.append("Lagrangian")
                            else:
                                time_best_y.append("Linear")

                            i = i+1

        fig = plt.figure(figsize=(16, 9))
        fig.subplots_adjust(top=0.955,
                          bottom=0.145,
                          left=0.04,
                          right=0.985,
                          hspace=0.2,
                          wspace=0.2)
        y = error_lag_y + error_linear_y + error_asc_y
        y = sorted(y)
        x = error_lag + error_linear + error_asc
        x = sorted(x)

        clrs = []
        for y_tick in y :
            if y_tick.__contains__("lgr"):
                clrs.append("indianred")
            elif y_tick.__contains__("lin"):
                clrs.append("limegreen")
            else:
                clrs.append("royalblue")

        plt.bar(y, x, color=clrs)
        plt.xlabel("Casistica", )
        plt.xticks(rotation=90)
        plt.ylabel("Errori relativi")
        plt.title("Errori a confronto")
        fig.savefig("Img2/CFL/error.png", format="png")

        fig_lgr = plt.figure(figsize=(16, 9))
        plt.bar(sorted(error_lag_y),sorted(error_lag))
        plt.xlabel("Casistica",)
        plt.xticks(rotation=90)
        plt.ylabel("Errori relativi")
        plt.title("Errori rilassamento lagreangiano")
        fig_lgr.savefig("Img2/CFL/error_lgr.png", format="png")

        fig_lin = plt.figure(figsize=(16, 9))
        plt.bar(sorted(error_linear_y), sorted(error_linear))
        plt.xlabel("Casistica", )
        plt.xticks(rotation=90)
        plt.ylabel("Errori relativi")
        plt.title("Errori rilassamento lineare")
        fig_lin.savefig("Img2/CFL/error_lin.png", format="png")

        fig_asc = plt.figure(figsize=(16, 9))
        plt.bar(sorted(error_asc_y), sorted(error_asc))
        plt.xlabel("Casistica", )
        plt.xticks(rotation=90)
        plt.ylabel("Errori relativi")
        plt.title("Errori AAD")
        fig_asc.savefig("Img2/CFL/error_asc.png", format="png")

        name_list = ["Linear","Lagrangian","AAD"]
        value = [error_best_y.count("Linear"),error_best_y.count("Lagrangian"),error_best_y.count("AAD")]
        circle = plt.Circle((0, 0), 0.7, color='white')
        fig_circle = plt.figure()
        figure = plt.pie(value, labels=name_list, wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
        plt.title("Errori relativi a confronto")
        p = plt.gcf()
        p.gca().add_artist(circle)
        plt.gcf().set_size_inches(7, 7)
        fig_circle.savefig("Img2/CFL/circle.png", format="png")

        value = [time_best_y.count("AAD")]
        circle = plt.Circle((0, 0), 0.7, color='white')
        fig_circle_time = plt.figure()
        figure_time = plt.pie(value, labels=["AAD"], wedgeprops={'linewidth': 7, 'edgecolor': 'white'})
        plt.title("Tempi a confronto")
        p = plt.gcf()
        p.gca().add_artist(circle)
        plt.gcf().set_size_inches(7, 7)
        fig_circle_time.savefig("Img2/CFL/circle_time.png", format="png")


    def plot_boxplot_time_cfl(self,dataset,name):
        filter_dataset = dataset[['times_linear', 'times_lagrange', 'times_asc']]
        filter_dataset = filter_dataset.copy()
        filter_dataset.rename(
            columns={ 'times_linear': 'linear', 'times_lagrange': 'lagrange',
                     'times_asc': 'AAD'}, inplace=True)

        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=45, fontsize=17)

        plt.ylabel("Tempo esecuzione",fontsize=20)
        plt.title("Andamento tempi", fontsize=20)

        fig.savefig("Img2/CFL/{name}.png".format(name=name), format="png")


    def plot_lineplot_solution_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label= "optimal")
        plt.plot(dataset['dimention'], dataset['solutions linear'], label= "linear")
        plt.plot(dataset['dimention'], dataset['solutions lgr'], label="lagrange")

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Costi complessivi",fontsize=20)
        plt.title("Andamento ottimo e rilassamenti", fontsize=20)
        plt.grid()
        plt.legend(fontsize=15)

        fig.savefig("Img2/CFL/line_plot_solution.png", format="png")

    def plot_lineplot_ascent_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label="optimal")
        plt.plot(dataset['dimention'], dataset['solutions asc'], label="dual ascent")

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Costi complessivi",fontsize=20)
        plt.title("Confronto AAD-PLI", fontsize=20)
        plt.grid()
        plt.legend(fontsize=15)

        fig.savefig("Img2/CFL/plot_lineplot_ascent.png", format="png")

    def plot_lineplot_time_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        area = (20 * np.random.rand(len(dataset['dimention']))) ** 2

        plt.scatter(dataset['dimention'], dataset['times opt'], label="optimal", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times asc'], label="dual ascent", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times lgr'], label="lagrange", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times linear'], label="linear", s=area ,alpha=0.5)

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Tempi esecuzione",fontsize=20)
        plt.title("Confronto tempi esecuzione",fontsize=20)
        plt.grid()
        plt.legend(fontsize=15)

        fig.savefig("Img2/CFL/plot_lineplot_time.png", format="png")

    def plot_error_solution_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")

        solution_opt = np.array(dataset['solutions opt'])
        solution_lgr = np.array(dataset['solutions lgr'])
        solution_linear = np.array(dataset['solutions linear'])
        solution_asc = np.array(dataset['solutions asc'])

        error_lagrange = (solution_opt-solution_lgr)/solution_opt
        error_linear = (solution_opt-solution_linear)/solution_opt
        error_asc = (solution_opt-solution_asc)/solution_opt

        fig = plt.figure(figsize=[10, 15])
        plt.scatter(dataset['dimention'],error_lagrange, label = "lagrange", s=200)
        plt.scatter(dataset['dimention'],error_linear, label = "lineare", s=100)
        plt.scatter(dataset['dimention'],error_asc, label = "ascesa duale", s=150)

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Errori relativi",fontsize=20)
        plt.title("Errori commessi",fontsize=20)
        plt.legend(fontsize=15)
        plt.grid()

        fig.savefig("Img2/CFL/plot_error.png", format="png")