from math import comb

p = 0.12
n = 10
def calc_p(n, k, p):
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

p1 = sum(calc_p(n, k, p) for k in range(3))
print(round(p1, 3))

p2 = sum(calc_p(n, k, p) for k in range(2, n+1))
print(round(p2, 3))
