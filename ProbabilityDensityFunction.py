# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""
    Use rejection method to generate random number from the probabilty density 
    function of f(x) = 2π*sin(4π*x)
"""
#-----------------------------------------------------------------------
#                       Additional Documentation
#
# RCS Revision Code:
#   $Id: ProbabilityDensityFunction.py,v 1.0 2019/04/21
#
# Modification History:
# - 20 Apr 2019:  Original by DJ Wadhwa
#
# Notes:
# - Written for Python 3.7
# - See import statements throughout for more information on non-
#   built-in packages and modules required.
#
# Copyright (c) 2019 by DJ Wadhwa.
#=======================================================================


#---------------- Module General Import and Declarations ---------------
import numpy as np
import matplotlib.pyplot as plt
import random as r

#create f(x) = 2π*sin(4π*x) 
def func(x):
    return 2*np.pi*np.sin(4*np.pi*x)

#create x axis with 1000 elements
x_axis  = np.arange(1000)*.00025

#create array to store func values
func_array = np.zeros(np.size(x_axis))

#calucalate f(x) from 0 to 0.25
for i in range (np.size(func_array)):
    func_array[i] = func(x_axis[i])

#use a rejection method to generate a random number
def rej():
    
    #rand is a uniform random number from 0 to 0.25
    rand = r.uniform(0, 0.25)
    
    #rand2 is a uniform random number from 0 to 2π
    rand2 = r.uniform(0, 2*np.pi)
    
    #if f(rand) > rand then return rand
    if (func(rand) > rand2):
        return rand
    
    #else make a recursive call to rej()
    else:
        return rej()
    
#create list of 1000 randomly generated values
rand_list = np.zeros(1000)

#generate values for rand_list
for i in range (1000):
    rand_list[i] = rej()
    
#generate a figure
fig1 = plt.figure()

#generate axes for plot
ax1 = fig1.add_axes((0.04, 0.05, 0.45, 0.45))

#plot f(x)
ax1.plot(x_axis, func_array)

#set title for plot
ax1.set_title("Plotting f(x) from 0 to 2π")

#create axes for histogram
ax2 = fig1.add_axes((0.525, 0.5, 0.45, 0.45))

#hist for rand_list
ax2.hist (rand_list)

#set title for histogram
ax2.set_title("Probabilty Density Function Histogram")

#show figure
fig1.show()