import numpy as np
import matplotlib.pyplot as plt
import random as r

def func(x):
    return 2*np.pi*np.sin(4*np.pi*x)

x_axis  = np.arange(100)*.0025
func_array = np.zeros(np.size(x_axis))

for i in range (np.size(func_array)):
    func_array[i] = func(x_axis[i])
    
def rej():
    rand = r.uniform(0, 0.25)
    rand2 = r.uniform(0, 2*np.pi)
    if (func(rand) > rand2):
        return rand
    else:
        return rej()
        
rand_list = np.zeros(1000)
for i in range (1000):
    rand_list[i] = rej()

fig1 = plt.figure()
ax1 = fig1.add_axes((0.04, 0.05, 0.45, 0.45))
ax1.plot(x_axis, func_array)
ax1.set_title("Plotting f(x)")

ax2 = fig1.add_axes((0.525, 0.5, 0.45, 0.45))
ax2.hist (rand_list)
ax2.set_title("probabilty desity function histogram")
fig1.show()