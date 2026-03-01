n = int(input().strip())

values = list(map(int, input().strip().split()))
weights = list(map(int, input().strip().split()))

w_sum = 0
t_weights = 0

for i in range(n):
    w_sum+= values[i]* weights[i]
    t_weights+= weights[i]

w_mean = w_sum /t_weights

print(f"{w_mean:.1f}")