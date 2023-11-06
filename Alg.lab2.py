import matplotlib.pyplot as plt

dataset_file = 'DS0.txt'

x_axis = []
y_axis = []

with open(dataset_file, 'r') as file:
    for line in file:
        x, y = map(int, line.strip().split())
        x_axis.append(x)
        y_axis.append(y)

plt.figure(figsize=(9.6, 5.4))

plt.scatter(x_axis, y_axis, marker='D', color='black')

plt.gca().invert_yaxis()
plt.axis('off')

plt.show()

plt.close()
