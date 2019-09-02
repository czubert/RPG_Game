import glob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()

final_results = []

for file in sorted(glob.glob('results/*')):
    with open(file, 'r') as f:
        lines = f.readlines()
        final_results.extend([line.split(',') for line in lines])

data = np.array(final_results)
col = 3

data = data[np.argsort(data[:, col])]

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
