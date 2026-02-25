import math
def get_numbers():
    m_input =input("plz enter the values")
    H_rates=[]
    for i in m_input.strip().split(","):
        try:
            H_rates.append(int(i))
        except ValueError:
            print(f"{i} Invalid input ")
            return None
    if not H_rates:
        print("no valid input")
        return None
    return H_rates

def find_min(H_rates):
    min_n = H_rates[0]
    for r in H_rates:
        if r < min_n:
            min_n = r
    return min_n

def find_max(H_rates):
    max_n = H_rates[0]
    for r in H_rates:
        if r > max_n:
            max_n = r
    return max_n


def find_mean(H_rates):
    sum = 0
    n= 0
    for r in H_rates:
        sum += r
        n += 1
    return sum / n

def find_mode(H_rates):
    freq = {}
    for r in H_rates:
        if r in freq:
            freq[r] += 1
        else:
            freq[r] = 1
    max_freq= 0
    for i in freq.values():
        if i > max_freq:
            max_freq = i
    mode =[]
    for key, val in freq.items():
        if val == max_freq:
            mode.append(key)
    return mode

def MySort(H_rates):
    temp= H_rates[:] 
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] > temp[j]:
                temp[i], temp[j] = temp[j], temp[i]
    return temp    

def find_median(H_rates):
    S_rates = MySort(H_rates) 
    n = len(S_rates)
    mid = n // 2
    if n % 2 == 0:
        return (S_rates[mid-1] + S_rates[mid])/2
    else:
        return S_rates[mid]
    

def find_range(H_rates):
    return find_max(H_rates)- find_min(H_rates)

def find_variance(H_rates):
    mean_r= find_mean(H_rates)
    t_val = 0
    for r in H_rates:
        t_val += (r - mean_r)** 2
    return t_val/(len(H_rates)-1)

def find_STD(H_rates):
    return math.sqrt(find_variance(H_rates))


def find_Quartiles(H_rates):
    nums = MySort(H_rates)
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        l_half = nums[:mid]
        u_half = nums[mid:]
    else:
        l_half = nums[:mid]
        u_half = nums[mid+1:]
    Q1= find_median(l_half)
    Q2= find_median(nums)
    Q3= find_median(u_half)
    return (Q1, Q2, Q3)


def find_IQR(numbers):
    Q1, Q2, Q3 = find_Quartiles(numbers)
    return Q3-Q1

heart_rates = get_numbers()
if heart_rates is not None:
    print("Min heart rate:",find_min(heart_rates))
    print("Max heart rate:",find_max(heart_rates))
    print("Mean heart rate:",round(find_mean(heart_rates), 2))
    print("Median:",find_median(heart_rates))
    print("Mode:", find_mode(heart_rates))
    print("Range:", find_range(heart_rates))
    print("Variance:",round(find_variance(heart_rates), 2))
    print("STD:", round(find_STD(heart_rates), 2))
    print("Quartiles:", find_Quartiles(heart_rates))
    print("IQR:", find_IQR(heart_rates))

