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
        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=90)

        plt.ylabel("Costi complessivi")
        plt.title("Andamento costi complessivi con problema di dimensione fissata")

        fig.savefig("Img/UFL/box_plot_solution.png", format="png")

    def plot_boxplot_time_ufl(self):
        filter_dataset = self.dataset_ufl[['times opt', 'times linear', 'times lagrange', 'times ascent']]
        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=90)

        plt.ylabel("Tempo esecuzione")
        plt.title("Andamento tempi esecuzione con problema di dimensione fissata")

        fig.savefig("Img/UFL/box_plot_time.png", format="png")

    def plot_boxplot_solution_cfl(self):
        filter_dataset = self.dataset_cfl[['solutions opt', 'solutions linear', 'solutions lagrange', 'solutions ascent']]
        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=90)

        plt.ylabel("Costi complessivi")
        plt.title("Andamento costi complessivi con problema di dimensione fissata")

        fig.savefig("Img/CFL/box_plot_solution.png", format="png")

    def plot_boxplot_time_cfl(self):
        filter_dataset = self.dataset_cfl[['times opt', 'times linear', 'times lagrange', 'times ascent']]
        fig = plt.figure(figsize=[10, 15])
        filter_dataset.boxplot(rot=90)

        plt.ylabel("Tempo esecuzione")
        plt.title("Andamento tempi esecuzione con problema di dimensione fissata")

        fig.savefig("Img/CFL/box_plot_time.png", format="png")

    def plot_lineplot_solution_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label= "optimal")
        plt.plot(dataset['dimention'], dataset['solutions linear'], label= "linear")
        plt.plot(dataset['dimention'], dataset['solutions lgr'], label="lagrange")

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Costi complessivi")
        plt.title("Andamento soluzione ottima e rilassamenti")
        plt.grid()
        plt.legend()

        fig.savefig("Img/UFL/line_plot_solution.png", format="png")

    def plot_lineplot_ascent_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label="optimal")
        plt.plot(dataset['dimention'], dataset['solutions asc'], label="dual ascent")

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Costi complessivi")
        plt.title("Confronto AAD-PLI")
        plt.grid()
        plt.legend()

        fig.savefig("Img/UFL/plot_lineplot_ascent.png", format="png")

    def plot_lineplot_time_ufl(self):
        dataset = pd.read_csv("CSV/UFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        area = (30 * np.random.rand(len(dataset['dimention']))) ** 2

        plt.scatter(dataset['dimention'], dataset['times opt'], label="optimal", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times asc'], label="dual ascent", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times lgr'], label="lagrange", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times linear'], label="linear", s=area ,alpha=0.5)

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Tempi esecuzione")
        plt.title("Confronto tempi esecuzione")
        plt.grid()
        plt.legend(fontsize=16)

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

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Errori relativi")
        plt.title("Errori commessi")
        plt.legend()
        plt.grid()

        fig.savefig("Img/UFL/plot_error.png", format="png")

    def plot_lineplot_solution_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label= "optimal")
        plt.plot(dataset['dimention'], dataset['solutions linear'], label= "linear")
        plt.plot(dataset['dimention'], dataset['solutions lgr'], label="lagrange")

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Costi complessivi")
        plt.title("Andamento soluzione ottima e rilassamenti")
        plt.grid()
        plt.legend()

        fig.savefig("Img/CFL/line_plot_solution.png", format="png")

    def plot_lineplot_ascent_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        plt.plot(dataset['dimention'], dataset['solutions opt'], label="optimal")
        plt.plot(dataset['dimention'], dataset['solutions asc'], label="dual ascent")

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Costi complessivi")
        plt.title("Confronto AAD-PLI")
        plt.grid()
        plt.legend()

        fig.savefig("Img/CFL/plot_lineplot_ascent.png", format="png")

    def plot_lineplot_time_cfl(self):
        dataset = pd.read_csv("CSV/CFL/complex.csv")
        fig = plt.figure(figsize=[10, 15])
        area = (20 * np.random.rand(len(dataset['dimention']))) ** 2

        plt.scatter(dataset['dimention'], dataset['times opt'], label="optimal", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times asc'], label="dual ascent", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times lgr'], label="lagrange", s=area ,alpha=0.5)
        plt.scatter(dataset['dimention'], dataset['times linear'], label="linear", s=area ,alpha=0.5)

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Tempi esecuzione")
        plt.title("Confronto tempi esecuzione")
        plt.grid()
        plt.legend(fontsize=16)

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

        plt.xlabel("Variabili decisionali")
        plt.ylabel("Errori relativi")
        plt.title("Errori commessi")
        plt.legend()
        plt.grid()

        fig.savefig("Img/CFL/plot_error.png", format="png")