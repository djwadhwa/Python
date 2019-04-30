# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""
    Find area under f(n) and Rn given polymer that uses random walk and 
    terminates if it crosses itself. 
    f(n) is the fraction of times the simulation generates a polymer of a given
    length. Rn is the root-mean-square displacement of the polymer
"""
#-----------------------------------------------------------------------
#                       Additional Documentation
#
# RCS Revision Code:
#   $Id: montecarlo2.py,v 1.0 2019/04/29
#
# Modification History:
# - 29 Apr 2019:  Original by DJ Wadhwa
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
import numpy as N
import matplotlib.pyplot as plt

#number of tests to perform
N_TESTS = 20000

#randomWalker partly derived from provided sample code
def randomWalkPoints(n):
    output_list_x = N.zeros((n,), dtype='l')
    output_list_y = N.zeros((n,), dtype='l')

    rand = N.random.randint(2, size=(n-1,))
    output_list_x[1:] = N.where(rand == 0, 1, -1)[:]
    output_list_x = N.cumsum(output_list_x)

    rand = N.random.randint(2, size=(n-1,))
    output_list_y[1:] = N.where(rand == 0, 1, -1)[:]
    output_list_y = N.cumsum(output_list_y)
    
    #treverse through both arrays
    for i in range (N.size(output_list_x)):
        
        #treverse through both arrays again to compare value
        for j in range (i+1, N.size(output_list_x)):
            
            #if values are equal, remove values that come after the 
            # cross overpoint
            if (output_list_x[i] == output_list_x[j] and 
            output_list_y[i] == output_list_y[j]):

            #shrink the array and break the loop
                    output_list_x = output_list_x[:j]
                    output_list_y = output_list_y[:j]
                    break
    
    #return both arrays
    return (output_list_x, output_list_y)

#calculate the distance between 2 endpoints 
def randomWalkDistance(x_points, y_points):
    return N.sqrt(x_points[-1]**2 + y_points[-1]**2)

#create a range to store f(n) value
frange = [0,]*N_TESTS
counter = 0 #count the number of times 
n = 4 #n value to test for

#run 20000 tests
for i in range (N_TESTS):
    
    #retrive random walk points with upto 20 steps
    xpts,ypts = randomWalkPoints(20)
    
    #if steps matches n, then increment counter
    if (N.size(xpts) == n):
        counter += 1
    #store continuous value of f(n)
    frange [i] = counter/N_TESTS
    
#create figure and axes
fig1, ax1 = plt.subplots()

#plot
ax1.plot(range(N_TESTS), frange)

#set x,y labels and title
ax1.set_xlabel("Number of Tests")
ax1.set_ylabel ("f(n)")
ax1.set_title ("f(n) as number of tests increases")

#show figure
fig1.show()

#store values for Rn
Rn = [0,]*19

#list of sums
Sn = [0,]

#change number of steps to look for
for i in range(1,20):
    
    #set counter similar to frange
    counter = 0
    
    #perform 20000 tests
    for j in range (N_TESTS):
        
        #call randomwWalkPoints with 20 steps
        xpts,ypts = randomWalkPoints(20)
        
        #if the random walk matches i, then increment counter, and add to 
        #list of sums
        if (N.size(xpts) == i):
            counter+=1
            Sn.append(randomWalkDistance (xpts, ypts)**2)
    #store sums in a list of Rn values
    Rn[i-1] = N.sqrt(N.sum(Sn[1:N.size(Sn)])/counter)
    
    #reset sums
    Sn = [0,]

#create figure and axes
fig2, ax1 = plt.subplots()

#plot
ax1.plot (range(1,20), Rn)

#set x,y labels and title
ax1.set_xlabel("Size of polymer")
ax1.set_ylabel ("root-mean-square displacement (Rn)")
ax1.set_title ("Rn as size of polymer increases")

#show figure
fig2.show()

