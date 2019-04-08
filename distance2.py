import numpy as N

def distance(x, y, pt):
    output_shape = (N.size(y), N.size(x))
    xall= N.resize(x,output_shape)
    yall = N.reshape (N.repeat(y,N.size(x)), output_shape)
    return (((xall-pt[0])**2) + ((yall-pt[1])**2))**.5