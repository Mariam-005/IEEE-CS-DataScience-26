import math
mean = 20  
gap = 2    
def area(x, mean, gap):
    return 0.5 * (1 + math.erf((x - mean)/(gap * math.sqrt(2))))

g1 = area(19.5, mean, gap)
print(round(g1, 3))

g2 = area(22, mean, gap)-area(20, mean, gap)
print(round(g2, 3))