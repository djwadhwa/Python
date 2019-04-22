import random as r
import numpy as np
import matplotlib.pyplot as plt

x_range = 1.5
y_range = 2.0

samples = np.arange(1,1000)
graph_area = x_range*y_range
total_percentage = np.zeros(np.size(samples))
error_array = np.zeros(np.size(total_percentage))
for i in range (np.size(samples)):
    under = 0
    for j in range (samples[i]):
        x = r.uniform(0,2)
        y = r.uniform(0,1.5)
        if (y < np.sqrt(np.cos(x)**2+1)):
            under += 1
    total_percentage[i]= (under/samples[i])*graph_area
    error_array[i] = np.std(total_percentage)

plt.plot(samples, error_array)
plt.show()