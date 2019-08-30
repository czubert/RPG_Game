import glob
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np

# TODO: you use libraries in a project - create a requirements.txt file and list them there with their version numbers
#  like:
#  some_magical_library==4.3.1
final_results = []

for file in sorted(glob.glob('results/*')):
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:  # TODO: It's better to use extend (its way faster and doesn't require loop)
            final_results.append(line.split(','))

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
