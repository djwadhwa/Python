# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""
    Use Box-Muller-Gauss Method to create a normal distribution of randomly
    generated floating point numbers from 0 to 2π
"""
#-----------------------------------------------------------------------
#                       Additional Documentation
#
# RCS Revision Code:
#   $Id: BoxMullerGauss.py,v 1.0 2019/04/21
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

#set constantds
mean = 9
stdDev = 2
size = 500
a = 0
b = 0

#create arrays
first_cord = np.zeros(size)
second_cord = np.zeros(size)
tblGauss = np.zeros(2*size)

#iterate through both coordinate arrays
for i in range (size):
    
    #generate a & b
    a = r.uniform (0, 2*np.pi)
    b = stdDev*np.sqrt(-1*np.log(r.random()))
    
    #calculate the value of both coordinates
    first_cord[i] = (b*np.sin(a)+mean)
    second_cord[i] = (b*np.cos(a)+mean)

#combine and flatten both arrays using for loop
for i in range (2*size):
    if i < size:
        tblGauss[i] = first_cord[i]
    else:
        tblGauss[i] = second_cord[i-size]

#combine and flatten both arrays using numpy function
tblGauss2 = np.concatenate((first_cord, second_cord))

#generate a figure
fig1 = plt.figure()

#create axes to display both histograms
ax1 = fig1.add_axes((0.075, 0.05, 0.4, 0.4))
ax2 = fig1.add_axes((0.55, 0.05, 0.4, 0.4))

#generate histograms
ax1.hist (tblGauss)
ax2.hist (tblGauss2)

#set titles
ax1.set_title("for loop to concatenate")
ax2.set_title("numpy function to concatenate ")

#show figure
fig1.show()