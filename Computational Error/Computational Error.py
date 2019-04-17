# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""
    Calculate relative and absolute error between analytical value 
    and numerical value for each year. Furthermore graph the analytical and 
    numerical values on the same axes in the same figure.
"""
#-----------------------------------------------------------------------
#                       Additional Documentation
#
# RCS Revision Code:
#   $Id: Computational Error.py,v 1.0 2019/04/17
#
# Modification History:
# - 16 Apr 2019:  Original by DJ Wadhwa
#
# Notes:
# - Written for Python 3.7
# - See import statements throughout for more information on non-
#   built-in packages and modules required.
#
# Copyright (c) 2019 by DJ Wadhwa.
#=======================================================================


#---------------- Module General Import and Declarations ---------------

#- Set module version number etc. to package version number etc.:
import numpy as np #used for arrays
import matplotlib.pyplot as plt #used for plotting

#set variables 
growth_rate = 0.093 
principal = 500.
time_frames = (10, 20, 30,40) # create an array of years to calculate

#set arrays to fill in data
calculated_array = np.zeros (np.size(time_frames))
absolute_error= np.zeros (np.size(time_frames))
relative_error = np.zeros (np.size(time_frames))
analytic_array = np.zeros (np.size(time_frames))

#first for loop used to calcualate analytical value for each time frame 
#by using P*e^(r*t) where e is the value from numpy
for i in range(np.size(time_frames)):
    calculated_array[i] = principal*np.exp(growth_rate*time_frames[i])
    
    #use this to manually calculate the value of e, which intentionally
    #introduces error. This reflects the numerical value
    for n in range (1, 100):
        #e = lim n->infinity (1+1/n)^(1*n)
        analytic_array [i] = principal*(1+ (growth_rate/n))**(n*time_frames[i])
        
#used to calculate both types of errors simultaneously
for i in range (np.size(time_frames)):
    
    #relative error = ((correct - result)/correct)*100
    relative_error[i] = ((calculated_array[i]-analytic_array[i])*100)/calculated_array[i]
    
    #abosulte error = |correct - result|
    absolute_error[i] = np.absolute(calculated_array[i]-analytic_array[i])
    
    #orint result to console
    print ("years", time_frames[i], "relative error:", str(relative_error[i])+"%","absolute error:", absolute_error[i])

#plot both lines to the same axes in the same figure
plt.plot(time_frames, calculated_array)
#dotted line to reflect analytical graph oveer calulated graph
plt.plot(time_frames, analytic_array, ":") 

#labels
plt.xlabel("Time (Years)")
plt.ylabel("Inverment value ($)")

#title
plt.title("Investment value over time")

#legend for both lines
plt.legend(['Calculated', 'Analytical'])

#display plot after running program
plt.show()