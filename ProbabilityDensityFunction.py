# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""
    Find area under f(x) = sqrt(cos^2(x)+1) using probabily by "throwing" darts
    uniformly on the graph containing f(x), where x ranges from 0 to 2 and y 
    ranges from 0 to 1.5, and caluclating number of darts under the cover
    compared to total darts, then multiplying this ratio with the area of the
    graph.
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
    
#generate a figure
fig1 = plt.figure()

#generate axes for plot
ax1 = fig1.add_axes((0.04, 0.05, 0.45, 0.45))
ax1.plot(x_axis, func_array)
ax1.set_title("Plotting f(x)")

#create
ax2 = fig1.add_axes((0.525, 0.5, 0.45, 0.45))
ax2.hist (rand_list)
ax2.set_title("probabilty desity function histogram")
fig1.show()