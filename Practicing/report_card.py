marks = []
print("Enter marks of subjects: ")
for i in range(5):
    marks.append(int(input("")))

def total(x):
    return sum(x)

def avg(x):
    return sum(x)/len(x)

def cgpa(x):
    credited_marks = []
    credit = [2 for i in range(len(x))]
    for i in range(5):
        credited_marks.append(credit[i]*x[i])
    return sum(credited_marks)/sum(credit*10)

def result(x):
    percentage = (total(x)/(len(x)*100))*100
    if percentage >= 35: 
        return "Pass"
    else:
        return "Fail"

report_card = {
    "Total": total(marks),
    "Average": avg(marks),
    "CGPA": cgpa(marks),
    "Pass/Fail": result(marks)
}
print(report_card)