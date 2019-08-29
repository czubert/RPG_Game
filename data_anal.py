import glob
import matplotlib.pyplot as plt

for file in sorted(glob.glob('results/*')):
    result = []
    tmp_result = []
    with open(file, 'r') as f:
        for line in f:
            tmp_result.append(line.split('\t+'))
        result.append(tmp_result)
        tmp_result = 'ss'
    print(f'{result}')
    print(tmp_result)
