n = int(input())
INlist = []

for _ in range(n):
    IN_L = input().split()
    
    match IN_L[0]:
        case "insert":
            INlist.insert(int(IN_L[1]), int(IN_L[2]))
        case "print":
            print(INlist)
        case "remove":
            INlist.remove(int(IN_L[1]))
        case "append":
            INlist.append(int(IN_L[1]))
        case "sort":
            INlist.sort()
        case "pop":
            INlist.pop()
        case "reverse":
            INlist.reverse()
