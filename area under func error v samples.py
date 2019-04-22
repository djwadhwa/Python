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
#   $Id: AreaUnderFuncErrorvSamples.py,v 1.0 2019/04/21
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

#- Set module version number etc. to package version number etc.:
import random as r
import numpy as np
import matplotlib.pyplot as plt

#create range for the x and y axis
x_range = 1.5
y_range = 2.0

#sample with upto 1000 darts
samples = np.arange(1,1000)

#calculate graph area with x and y range
graph_area = x_range*y_range

#create array for percentage of darts under line
total_percentage = np.zeros(np.size(samples))

#array for standard deviation of total_percentage
error_array = np.zeros(np.size(total_percentage))

#iterate from 1 dart to 1000 dart samples
for i in range (np.size(samples)):
    
    #counter for darts under the line
    under = 0
    
    #generate darts 
    for j in range (samples[i]):
        
        #generate randam x and y value for darts
        x = r.uniform(0,2)
        y = r.uniform(0,1.5)
        
        #if the random coordinate was under f(x), increment counter
        if (y < np.sqrt(np.cos(x)**2+1)):
            under += 1
    
    #calcualate the value of f(x)
    total_percentage[i]= (under/samples[i])*graph_area
    
    #calcualte the erro
    error_array[i] = np.std(total_percentage)

#plot error to samples
plt.plot(samples, error_array)

#label axes
plt.xlabel("Number of darts")
plt.ylabel("Error")

#set title
plt.title("Error vs Number of Samples")

#show plot
plt.show()