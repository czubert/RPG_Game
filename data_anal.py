import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

sns.set()


class DataAnalysis:
    def __init__(self):
        self.final_results = []

    def analise_data(self, col_x, col_y, x_title, y_title):
        """
        Runs sequence of methods. Clears data, sort it and makes a plot.
        :param col: int
        :return: None
        """
        self.split_data_for_analysis()
        self.create_a_plot(col_x, col_y, x_title, y_title)

    @staticmethod
    def read_data_for_analysis():
        """
        Takes all files from folder 'results', reads it line by line and splits every each line into separate list
        :return: None
        """
        tmp_results = []
        for file in sorted(glob.glob('results/*')):
            with open(file, 'r') as f:
                tmp_results.extend(f.readlines())
            print(tmp_results)
        return tmp_results

    def split_data_for_analysis(self):
        self.final_results.extend([line.split(',') for line in self.read_data_for_analysis()])


    def create_a_plot(self, col_x, col_y, x_title, y_title):
        """
        Creates a plot from all files in 'results' folder
        :param data: NumPy array of arrays
        :return: None
        """
        print(self.final_results)
        data = np.array(self.final_results)

        x = data[:, col_x]
        y = data[:, col_y]
        print(x)
        print(y)

        x = x.astype(np.float)
        y = y.astype(np.float)

        # add title
        plt.title('Relationship Between number of rounds and time')

        # add x and y labels
        plt.xlabel(x_title)
        plt.ylabel(y_title)

        plt.plot(x, y, '.')
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
    data1.analise_data(3, 4,'Number of rounds', 'Duration of one round')
    data1.analise_data(3, 2,'Number of rounds', 'Number of players')
