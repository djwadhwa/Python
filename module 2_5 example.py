# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


#ordinary variables
mec = 10 #µg/ml       
mtc = 20 #µg/ml               
halfLife = 22 #hr       
volume = 3000 #ml   
dosage = 100 * 1000 #µg
absorptionFraction = 0.12   
interval = 8 #hr
start = 0 #hr

#derived stock variables
eliminationConstant = -np.log(.5)/halfLife #units: 1/hours  

#stock variables
drugInSystem = np.zeros(5040)
drugInSystem[0] = absorptionFraction * dosage #units: µg

simHrs = 168        
deltaX = 2/60       
x= np.arange(0,simHrs, deltaX)

def xtoi(x): 
    return x / deltaX + 1 
def itox(i):
    return (i - 1) * deltaX 

for i in range(1, np.size(x)): 
    if (itox(i)%interval == 0):
        ingested = absorptionFraction * dosage 
        print(itox(i))
    else:
        ingested = 0 
    eliminated = (eliminationConstant * drugInSystem[i - 1]) * deltaX 
    drugInSystem[i] = drugInSystem[i - 1] + ingested - eliminated 
 
concentration = drugInSystem / volume  
plt.plot(x, concentration)
plt.xlabel("hours")
plt.ylabel("concentration (µg/ml)")
plt.show()
