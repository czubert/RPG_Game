import glob
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np

# TODO: you use libraries in a project - create a requirements.txt file and list them there with their version numbers
#  like:
#  some_magical_library==4.3.1

for file in sorted(glob.glob('results/*')):
    final_results = []  # FIXME: you clear this list for every file, so only last file stays in memory
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:  # TODO: It's better to use extend (its way faster and doesn't require loop)
            final_results.append(line.split(','))

data = np.array(final_results)
col = 3
# FIXME: the data after reading are always always always strings. To make a good plot you need to get numbers

data = data[np.argsort(data[:, col])]  # FIXME: Whoa. I don't know what it is.

X = []
Y = []

# TODO: This would work properly, but you're mixing pythonic lists with numpy arrays.
#  In general, when you go to arrays - you keep it as an array. That's fine for now, but:
#  in numpy you can slice an array. whole third column is like: data[:,2]
#  : means "all" for first dimension (rows), 2 means 'second elements' in second dimesions (columns)

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
