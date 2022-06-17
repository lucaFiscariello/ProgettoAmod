import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class GraphicGenerator:
    def __init__(self):
        dataset_asc_ufl = pd.read_csv("CSV/UFL/ascent.csv")
        dataset_linear_ufl = pd.read_csv("CSV/UFL/linear.csv")
        dataset_lrg_ufl = pd.read_csv("CSV/UFL/lagrange.csv")
        dataset_opt_ufl = pd.read_csv("CSV/UFL/opt.csv")

        dataset_asc_cfl = pd.read_csv("CSV/CFL/ascent.csv")
        dataset_linear_cfl = pd.read_csv("CSV/CFL/linear.csv")
        dataset_lrg_cfl = pd.read_csv("CSV/CFL/lagrange.csv")
        dataset_opt_cfl = pd.read_csv("CSV/CFL/opt.csv")

        self.dataset_ufl = dataset_opt_ufl
        for dataset in [dataset_asc_ufl, dataset_linear_ufl, dataset_lrg_ufl ]:
            for column_name in dataset.columns:
                self.dataset_ufl.insert(0, column_name, dataset[column_name], allow_duplicates=True)

        self.dataset_cfl = dataset_opt_cfl
        for dataset in [dataset_asc_cfl, dataset_linear_cfl, dataset_lrg_cfl]:
            for column_name in dataset.columns:
                self.dataset_cfl.insert(0, column_name, dataset[column_name], allow_duplicates=True)


    def plot_boxplot_solution_ufl(self):
        filter_dataset = self.dataset_ufl[['solutions opt', 'solutions linear', 'solutions lagrange', 'solutions ascent']]
        filter_dataset = filter_dataset.copy()
        filter_dataset.rename(
            columns={'solutions opt': 'opt', 'solutions linear': 'linear', 'solutions lagrange': 'lagrange',
                     'solutions ascent': 'AAD'}, inplace=True)

        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=45, fontsize=17)

        plt.ylabel("Costi complessivi", fontsize=20)
        plt.title("Andamento costi",fontsize=20)

        fig.savefig("Img/UFL/box_plot_solution.png", format="png")

    def plot_boxplot_time_ufl(self):
        filter_dataset = self.dataset_ufl[['times opt', 'times linear', 'times lagrange', 'times ascent']]
        filter_dataset = filter_dataset.copy()
        filter_dataset.rename(
            columns={'times opt': 'opt', 'times linear': 'linear', 'times lagrange': 'lagrange',
                     'times ascent': 'AAD'}, inplace=True)

        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=45, fontsize=17)

        plt.ylabel("Tempo esecuzione", fontsize=20)
        plt.title("Andamento tempi", fontsize=20)

        fig.savefig("Img/UFL/box_plot_time.png", format="png")

    def plot_boxplot_solution_cfl(self):
        filter_dataset = self.dataset_cfl[['solutions opt', 'solutions linear', 'solutions lagrange', 'solutions ascent']]
        filter_dataset = filter_dataset.copy()
        filter_dataset.rename(
            columns={'solutions opt': 'opt', 'solutions linear': 'linear', 'solutions lagrange': 'lagrange',
                     'solutions ascent': 'AAD'}, inplace=True)

        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=45, fontsize=17)

        plt.ylabel("Costi complessivi",fontsize=20)
        plt.title("Andamento costi", fontsize=20)

        fig.savefig("Img/CFL/box_plot_solution.png", format="png")

    def plot_boxplot_time_cfl(self):
        filter_dataset = self.dataset_cfl[['times opt', 'times linear', 'times lagrange', 'times ascent']]
        filter_dataset = filter_dataset.copy()
        filter_dataset.rename(
            columns={'times opt': 'opt', 'times linear': 'linear', 'times lagrange': 'lagrange',
                     'times ascent': 'AAD'}, inplace=True)

        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=45, fontsize=17)

        plt.ylabel("Tempo esecuzione",fontsize=20)
        plt.title("Andamento tempi", fontsize=20)

        fig.savefig("Img/CFL/box_plot_time.png", format="png")

    def plot_lineplot_solution_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label= "optimal")
        plt.plot(dataset['dimention'], dataset['solutions linear'], label= "linear")
        plt.plot(dataset['dimention'], dataset['solutions lgr'], label="lagrange")

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Costi complessivi",fontsize=20)
        plt.title("Confronto ottimo e rilassamenti",fontsize=20)
        plt.grid()
        plt.legend(fontsize=15)

        fig.savefig("Img/UFL/line_plot_solution.png", format="png")

    def plot_lineplot_ascent_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label="optimal")
        plt.plot(dataset['dimention'], dataset['solutions asc'], label="dual ascent")

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Costi complessivi",fontsize=20)
        plt.title("Confronto AAD-PLI",fontsize=20)
        plt.grid()
        plt.legend(fontsize=15)

        fig.savefig("Img/UFL/plot_lineplot_ascent.png", format="png")

    def plot_lineplot_time_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        area = (30 * np.random.rand(len(dataset['dimention']))) ** 2

        plt.scatter(dataset['dimention'], dataset['times opt'], label="optimal", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times asc'], label="dual ascent", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times lgr'], label="lagrange", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times linear'], label="linear", s=area ,alpha=0.5)

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Tempi esecuzione",fontsize=20)
        plt.title("Confronto tempi esecuzione",fontsize=20)
        plt.grid()
        plt.legend(fontsize=15)

        fig.savefig("Img/UFL/plot_lineplot_time.png", format="png")

    def plot_error_solution_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")

        solution_opt = np.array(dataset['solutions opt'])
        solution_lgr = np.array(dataset['solutions lgr'])
        solution_linear = np.array(dataset['solutions linear'])
        solution_asc = np.array(dataset['solutions asc'])

        error_lagrange = (solution_opt-solution_lgr)/solution_lgr
        error_linear = (solution_opt-solution_linear)/solution_lgr
        error_asc = (solution_asc-solution_opt)/solution_opt

        fig = plt.figure(figsize=[10, 15])
        plt.scatter(dataset['dimention'],error_lagrange, label = "lagrange", s=200)
        plt.scatter(dataset['dimention'],error_linear, label = "lineare", s=100)
        plt.scatter(dataset['dimention'],error_asc, label = "ascesa duale", s=150)

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Errori relativi",fontsize=20)
        plt.title("Errori commessi", fontsize=20)
        plt.legend(fontsize=15)
        plt.grid()

        fig.savefig("Img/UFL/plot_error.png", format="png")

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

        fig.savefig("Img/CFL/line_plot_solution.png", format="png")

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

        fig.savefig("Img/CFL/plot_lineplot_ascent.png", format="png")

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

        fig.savefig("Img/CFL/plot_lineplot_time.png", format="png")

    def plot_error_solution_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")

        solution_opt = np.array(dataset['solutions opt'])
        solution_lgr = np.array(dataset['solutions lgr'])
        solution_linear = np.array(dataset['solutions linear'])
        solution_asc = np.array(dataset['solutions asc'])

        error_lagrange = (solution_opt-solution_lgr)/solution_lgr
        error_linear = (solution_opt-solution_linear)/solution_lgr
        error_asc = (solution_asc-solution_opt)/solution_opt

        fig = plt.figure(figsize=[10, 15])
        plt.scatter(dataset['dimention'],error_lagrange, label = "lagrange", s=200)
        plt.scatter(dataset['dimention'],error_linear, label = "lineare", s=100)
        plt.scatter(dataset['dimention'],error_asc, label = "ascesa duale", s=150)

        plt.xlabel("Variabili decisionali",fontsize=20)
        plt.ylabel("Errori relativi",fontsize=20)
        plt.title("Errori commessi",fontsize=20)
        plt.legend(fontsize=15)
        plt.grid()

        fig.savefig("Img/CFL/plot_error.png", format="png")