# -*- coding: utf-8 -*-

#=======================================================================
#                        General Documentation

"""Single-function module.

   See function docstring for description.
"""

#-----------------------------------------------------------------------
#                       Additional Documentation
#
# RCS Revision Code:
#   $Id: distance.py,v 1.0 2019/04/07
#
# Modification History:
# - 04 Apr 2019:  Original by DJ Wadhwa
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


#-------------------- General Function:  distance ---------------------
    
def distance (x_vector, y_vector, point):
    
    """
    Take a vector of x-locations and a vector of y-locations and calculate
    the distance at all points defined by those locations from a given point

    Method Arguments:
    * x-vector:  A vector of x locations where values are integers.
    * y-vector:  A vector of y locations where values are integers.
    * point:  A 2D point that distances are calculated from
    
    Output:
    * dist is a 2D array that contains float values of distance between the 
    location and the given point

    distance can be calculated by using the distance formula:
        d = √(((y1-y0)^2)+((x1-x0)^2))
    """
    #assinging variables to the length of x_vector and y_vector
    x_len = len(x_vector) 
    y_len = len(y_vector) 
    
    #creating a 2D array with the y_len rows and x_len columns
    dist = N.zeros([y_len, x_len]) 
    
    #traverse through dist array
    for i in range (y_len):
        for j in range (x_len):
            #use the distance function and use values from the vector directly
            #using (1/2) to find square root
            dist [i,j] = (((y_vector[i]-point[1])**2)+
            ((x_vector[j]-point[0])**2))**(1/2)
    
    #return dist array
    return dist
