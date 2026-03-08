import math

l= float(input()) 
k = int(input())    

result = (l**k * math.exp(-l)) / math.factorial(k)

print(round(result, 3))