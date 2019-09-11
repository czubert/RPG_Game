import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

sns.set()


class DataAnalysis:
    def __init__(self):
        self.final_results = []

    def analise_data(self):
        """
        Runs sequence of methods. Clears data, sort it and makes a plot.
        :param col: int
        :return: None
        """
        self.split_data_for_analysis()
        self.create_a_plot()

    @staticmethod
    def read_data_for_analysis():
        """
        Takes all files from folder 'results', reads it line by line and splits every each line into separate list
        :return: None
        """
        for file in sorted(glob.glob('results/*')):
            with open(file, 'r') as f:
                return f.readlines()

    def split_data_for_analysis(self):
        self.final_results.extend([line.split(',') for line in self.read_data_for_analysis()])
        print(self.final_results)

    def create_a_plot(self):
        """
        Creates a plot from all files in 'results' folder
        :param data: NumPy array of arrays
        :return: None
        """
        data = np.array(self.final_results)

        x = data[:, 3]
        y = data[:, 4]

        x = x.astype(np.float)
        y = y.astype(np.float)

        # add title
        plt.title('Relationship Between number of rounds and time')

        # add x and y labels
        plt.xlabel('Number of rounds')
        plt.ylabel('Duration of one round')

        plt.plot(x, y, 'o')
        self.trend_line(x, y)

    @staticmethod
    def trend_line(x, y):
        """
        Draws plot with trend line and labels
        :param x: array of floats
        :param y: array of floats
        :return:
        """
        slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
        line = slope * x + intercept

        plt.plot(x, line)
        plt.show()


if __name__ == '__main__':
    data1 = DataAnalysis()
    data1.analise_data()
