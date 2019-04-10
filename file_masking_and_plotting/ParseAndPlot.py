# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""
    Read ASFG_Ts.txt files, eliminate bad, inconsistent data and display plot
    as well print Mean, Median, and Standard Deviation. 
"""
#-----------------------------------------------------------------------
#                       Additional Documentation
#
# RCS Revision Code:
#   $Id: ParseAndPlot.py,v 1.0 2019/04/09
#
# Modification History:
# - 08 Apr 2019:  Original by DJ Wadhwa
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
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt

#create object that opens ASFG_Ts.txt as a readable file
fileobj = open("ASFG_Ts.txt",'r')

#read all the lines from the file object and save it in a list
temp_list = fileobj.readlines()

#create arrays for julian days and surface temperature
#4 elements smaller because first 3 lines are just column headers
# and the last line is empty
days = np.zeros(np.size(temp_list)-4)
temps = np.zeros(np.size(temp_list)-4)

#for loop starts from the 3rd line and goes to end of list -1
for line in range (3,np.size(temp_list)-1):
    
    #make a list of strings seperated by \t character
    data_list = temp_list[line].split ('\t')
    
    #data_list is 4 elements long if data is not bad
    if (len(data_list)==4):
        
        #subtract by 3 because of column headers
        #data_list [0] containts julian days
        days[line-3] = data_list [0]
        
        #data_list [3] contains surface temps
        #data list [3] is not a \n character or empty
        if (data_list[3] != '\n' and data_list[3] != ''):
            
            #set the floating point value to temps 
            temps[line-3] = data_list [3]
        else:
            #if it is next line character or empty set it to 10.00
            temps[line-3] = 10.00
    else:
        #if it is bad data set it to 10.00
        temps[line-3] = 10.00
        
#mask bad data which is marked as 10.00 in the temps array
temps = ma.masked_equal(temps, 10.00) 

#bad days are marked as 0 since the original array is all zeros
days = ma.masked_equal(days, 0)

# print the mean, median and std dev. of temperature using masked array library
print("Mean temperature:", ma.mean(temps))
print("Median temperature:", ma.median(temps))
print("Temperature standard deviation:", ma.std(temps))

#make a plot with days as x axis and temp as y axis
plt.plot (days, temps)

#set title for plot
plt.title("Surface Temperature vs. Julian Days")

#set x y labels for plot
plt.xlabel("Julian Days from 01/01/1997")
plt.ylabel("Surface Temparture (deg C)")

#display the plot
plt.show()

#close the file object
fileobj.close()
