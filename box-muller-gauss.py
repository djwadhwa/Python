import numpy as np
import matplotlib.pyplot as plt
import random as r

mean = 9
stdDev = 2
size = 500
a = 0
b = 0
first_cord = np.zeros(size)
second_cord = np.zeros(size)
tblGauss = np.zeros(2*size)

for i in range (size):
    a = r.uniform (0, 2*np.pi)
    b = stdDev*np.sqrt(-1*np.log(r.random()))
    first_cord[i] = (b*np.sin(a)+mean)
    second_cord[i] = (b*np.cos(a)+mean)

for i in range (2*size):
    if i < size:
        tblGauss[i] = first_cord[i]
    else:
        tblGauss[i] = second_cord[i-size]

tblGauss2 = np.concatenate((first_cord, second_cord))
fig1 = plt.figure()
ax1 = fig1.add_axes((0.075, 0.05, 0.4, 0.4))
ax1.hist (tblGauss)
ax1.set_title("Using for loop")

ax2 = fig1.add_axes((0.55, 0.05, 0.4, 0.4))
ax2.hist (tblGauss2)
ax2.set_title("Using concatenate")
fig1.show()