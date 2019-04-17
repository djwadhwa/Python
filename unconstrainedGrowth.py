simulationLength = 10
population = 200
growthRate = 0.1
deltaT = 0.005
growthRatePerStep = growthRate*deltaT
numIterations = simulationLength/deltaT
for i in range(1, int(numIterations)+1):
    growth = growthRate * population
    population = population + growth * deltaT
    t = i * deltaT

print (int(population))
