student_hours = {}
subject_hours = {}

with open('students.txt', 'r', encoding='utf-8') as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) == 3:
            name, hours, subject = data[0], int(data[1]), data[2]
            student_hours[name] = student_hours.get(name, 0) + hours
            subject_hours[subject] = subject_hours.get(subject, 0) + hours

top_student = ""
max_Shours = 0
for name,total in student_hours.items():
    if total > max_Shours:
        max_Shours = total
        top_student = name


most_subject = ""
max_subhours = 0
for subject, total in subject_hours.items():
    if total > max_subhours:
        max_subhours= total
        most_subject = subject

with open('summary.txt', 'w', encoding='utf-8') as out:
    out.write("Total hours per student \n")
    for name, total in student_hours.items():
        out.write(f" {name}: {total}\n")
        
    out.write("Total hours per subject:\n")
    for subj, total in subject_hours.items():
        out.write(f"  {subj}: {total}\n")
         
    out.write(f"top student: {top_student} with {max_Shours} hours\n")
    out.write(f"most studied subject: {most_subject} with {max_subhours} hours")