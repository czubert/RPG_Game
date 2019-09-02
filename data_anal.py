import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()


class DataAnalysis:
    def __init__(self):
        self.final_results = []

    def analise_data(self, col):
        self.split_data_for_analysis()
        data = self.sort_data(col)
        self.create_a_plot(data)

    def split_data_for_analysis(self):
        for file in sorted(glob.glob('results/*')):
            with open(file, 'r') as f:
                lines = f.readlines()
                self.final_results.extend([line.split(',') for line in lines])

    def sort_data(self, col):
        data = np.array(self.final_results)
        col = 3
        data = data[np.argsort(data[:, col])]
        return data

    def create_a_plot(self, data):
        X = data[:, 3]
        Y = data[:, 4]

        X = X.astype(np.float)
        Y = Y.astype(np.float)

        # scatter plot
        plt.scatter(X, Y, s=10, c='red')

        # add title
        plt.title('Relationship Between number of rounds and time')

        # add x and y labels
        plt.xlabel('Number of rounds')
        plt.ylabel('Duration of one round')

        # show plot
        plt.show()


data1 = DataAnalysis()

data1.analise_data(3)
