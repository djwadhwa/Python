# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

growth_rate = 0.093
principal = 500.
time_frames = (10, 20, 30,40)
calculated_array = np.zeros (np.size(time_frames))
absolute_error= np.zeros (np.size(time_frames))
relative_error = np.zeros (np.size(time_frames))
analytic_array = np.zeros (np.size(time_frames))

for i in range(np.size(time_frames)):
    calculated_array[i] = principal*np.exp(growth_rate*time_frames[i])
    for n in range (1, 100):
        analytic_array [i] = principal*(1+ (growth_rate/n))**(n*time_frames[i])
        
for i in range (np.size(time_frames)):
    relative_error[i] = ((calculated_array[i]-analytic_array[i])*100)/calculated_array[i]
    absolute_error[i] = np.absolute(calculated_array[i]-analytic_array[i])
    print ("years", time_frames[i], "relative error:", relative_error[i],"absolute error:", absolute_error[i])
    
plt.plot(time_frames, calculated_array)
plt.plot(time_frames, analytic_array, ":")
plt.xlabel("Years")
plt.ylabel("Inverment value")
plt.title("Investment value over time")
plt.legend(['Calculated', 'Analytical'])
plt.show()