# -*- coding: utf-8 -*-
import numpy as np

#ordinary variables
halfLife = 3.2 #units: hours
plasmaVolume = 3000 #units: ml

#derived stock variables
eliminationConstant = -np.log(.5)/halfLife #units: 1/hours

#stock variables
aspirinInPlasma= np.zeros(96)
aspirinInPlasma[0] = 2*365*1000 #units: µg

#flow variables
elimation = 0

simulationHours = 8
deltaX = 5/60

x= np.arange(0,simulationHours, deltaX)

def xtoi(x):  
    return x / deltaX + 1 

def itox(i):  
    return (i - 1) * deltaX

for i in range(1, np.size(x)):
    elimination = (eliminationConstant * aspirinInPlasma[i-1]) * deltaX
