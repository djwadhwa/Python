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
#   $Id: exponential_func.py,v 1.0 2019/04/08
#
# Modification History:
# - 05 Apr 2019:  Original by DJ Wadhwa
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

import math as M


#-------------------- General Function:  exponential ---------------------

def exponential(x, tol=1e-8):
    """
    Take a scalar input x and provide a scalar output of the exponential
    function

    Method Arguments:
    * x: a float or integer that is an input to an exponential function
    * tol: tolernace tht dictates the number of digits that follow the decimal 
    point when rounding
    
    Output:
    * answer that cointains the value of Euler's number raised to the power of x
    
    Example with tol:
        print (exponential (3.4, tol=1e-9))
        >>> 29.964100047
               ---------
               123456789 => 9 digits

    exponential function can be calculated by a series expansion represented 
    below:
                ∞
        e^x = Σ     (x^n)/(n!)
                n=0
    """
    #set answer and the number of digits following decimal point to 0
    answer = 0
    digits = 0
    
    #calculate the number of digits by mulitple tolerance by 10 while it is less
    #than 1
    while (tol <1):
       digits += 1
       tol *= 10
       
    #sum upto 50 times
    for n in range (50):
        
        #use math module's factorial function to calculate n!
        answer += (x**n)/M.factorial(n)
        
    #round answer by given nuumber of digits
    answer = round(answer, digits)
    
    #return rounded answer
    return answer
