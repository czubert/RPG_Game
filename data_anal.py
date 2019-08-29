import glob
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np

for file in sorted(glob.glob('results/*')):
    final_results = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            final_results.append(line.split(','))

data = np.array(final_results)
col = 3

data = data[np.argsort(data[:, col])]

X = []
Y = []

for rounds in data:
    X.append(rounds[3])  # number rounds
    Y.append(rounds[4])  # duration of round

# scatter plot
plt.scatter(X, Y, s=10, c='red')

# add title
plt.title('Relationship Between number of rounds and time')

# add x and y labels
plt.xlabel('Number of rounds')
plt.ylabel('Duration of one round')

# show plot
plt.show()
