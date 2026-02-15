
n = int(input( ))

Slist=[int(i) for i in input().split()]
# print(Slist)
Mscore=max(Slist)

targetN=0
for i in Slist:
    if i !=Mscore and i> targetN:
        targetN=i

print(targetN)        