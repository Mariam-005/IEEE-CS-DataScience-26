n = int(input( ))
grades = {}

for x in range(n):
    S_info= input().split()
    name =  S_info[0]
    scores = S_info[1:]

    F_score = []
    for i in scores:
        F_score.append(float(i))
    
    grades[name] = F_score

Q_name = input()
all_scores = grades[Q_name]
average = sum(all_scores) /len(all_scores)

print(f"{average:.2f}")
