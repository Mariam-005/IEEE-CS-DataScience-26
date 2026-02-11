num = int(input("Plz enter the num "))
n_digits = len(str(num))

final = 0
temp = num
while temp > 0:
    digit=temp % 10      
    final+= (digit**n_digits)
    temp //= 10       


if final == num:
    print(num , "is armstrong number")
else:
    print(num , "isn't armstrong number")
