#col 1 angle (radians), col 2 sine, col 3 cosine
#0 to pi
#sep by tab

import numpy as N
import matplotlib.pyplot as plt

def trigtable():
    myfile = open ("table.txt",'w')
    radians = N.arange(20) / 19.0 * 2 * N.pi
    sines = N.sin(radians)
    cos = N.cos(radians)
    
    for x in range (N.size(radians)):
        myfile.write (str(radians[x])+"\t"+str(sines[x])+"\t"+str(cos[x])+"\n")
    
    plt.plot (radians, sines, 'bo--')
    plt.axis ([0.0, 2*N.pi, -1, 1])
    plt.xlabel("Angle")
    plt.ylabel("Sine")
    plt.title("My Graph")
    plt.show()
    myfile.close()

trigtable()