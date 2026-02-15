n = int(input( ))

STlist = []
for _ in range(n):
    name = input()
    score = float(input())
    STlist.append([name, score])

scores = []
for student in STlist:
    scores.append(student[1])

U_scores =list(set(scores))
U_scores.sort()

target_score =U_scores[1]
target_name=[]
for student in STlist:
   if student[1]==target_score:
       target_name.append(student[0])

target_name.sort()
for i in target_name:
    print(i)



   
