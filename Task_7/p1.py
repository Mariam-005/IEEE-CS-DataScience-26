from math import comb

p_boy = 1.09 / 2.09
p_girl = 1 / 2.09
n = 6
result = sum(comb(n, k) * (p_boy**k) * (p_girl**(n-k)) 
    for k in range(3, n+1))

print(round(result, 3))