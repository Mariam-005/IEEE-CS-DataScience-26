import math

x1 = int(input("enter x1"))
y1 = int(input("enter y1"))
x2 = int(input("enter x2"))
y2 = int(input("enter y2"))

dx = x2 - x1
dy = y2 - y1
distance = math.sqrt(dx**2 + dy**2)

print(distance)
