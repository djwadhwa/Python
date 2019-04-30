import numpy as N

mu = [10, 15, 5, 15, 10]
stdev = [2.3, 2.8, 1.6, 2.8, 2.3]
start = [11,12,13,17,20]
end = [12,13,17,20,21]

p = N.zeros(N.size(mu))
n = N.zeros(N.size(mu))
ncas = N.zeros(N.size(mu))
pcas = N.zeros(N.size(mu))

for i in range (N.size(mu)):
    p[i] = 1 - (stdev[i]**2/mu[i])
    n[i] = mu[i]/p[i]
    ncas[i] = mu[i]*10

for k in range (N.size(mu)):
    if (k == 0):
        pcas[k] = .01
    else:
        pcas[k] = 0.1+ncas[k-1]*.002