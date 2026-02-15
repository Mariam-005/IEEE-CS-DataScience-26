t = int(input()) 

for i in range(t):
    try:
        nums = input().split()
        a = int(nums[0])
        b = int(nums[1])
        print(a // b)
    except Exception as e:
        print("Error Code:", e)
