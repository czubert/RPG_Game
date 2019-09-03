import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

sns.set()


class DataAnalysis:
    def __init__(self):
        self.final_results = []

    def analise_data(self, col):
        """
        Runs sequence of methods. Clears data, sort it and makes a plot.
        :param col: int
        :return: None
        """
        self.read_data_for_analysis()
        self.split_data_for_analysis()
        data = self.sort_data(col)
        self.create_a_plot(data)

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

    def sort_data(self, col):
        """
        Changes python list to NumPy array and sorts data with specific 'col'(column) as a parameter
        :param col: int
        :return: NumPy array
        """
        data = np.array(self.final_results)
        data = data[np.argsort(data[:, col])]
        return data

    def create_a_plot(self, data):
        """
        Creates a plot from all files in 'results' folder
        :param data: NumPy array of arrays
        :return: None
        """
        x = data[:, 3]
        y = data[:, 4]

        x = x.astype(np.float)
        y = y.astype(np.float)

        # add title
        plt.title('Relationship Between number of rounds and time')

        # add x and y labels
        plt.xlabel('Number of rounds')
        plt.ylabel('Duration of one round')

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

        plt.plot(x, y, 'o')
        plt.plot(x, line)
        plt.show()


data1 = DataAnalysis()

data1.analise_data(3)
