import numpy as np

sample = np.loadtxt("test.csv", delimiter=",", dtype="unicode")
print(sample)
print("--------------------")
print(type(sample))

for i in range(len(sample)):
    sample2 = sample[i][1].astype("int32")

print(type(sample[1][1]))
print(sample2)