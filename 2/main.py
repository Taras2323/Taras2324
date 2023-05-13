from students import Student

#1 single student
'''
student = Student("Dima", 14, "S2019")
print("Call artibutttes:\n")
print(f"Name: {student.Name}\n")
f"Age: {student.Age}\n"
f"Group: {student.Group}"
print("Call method ShowStudentInfo:")
student.ShowStudentInfo()
'''


#2 list of students
dimaS = Student("Dima", 14, "S2019")
antonS = Student("Anton", 10, "S2019")
dariiS = Student("Darii", 11, "S2019")
tarasS = Student("Taras", 14, "S2019")
tymurS = Student("Tymur", 13, "S2019")
students = list()
students.append(dimaS)
students.append(antonS)
students.append(dariiS)
students.append(tarasS)
students.append(tymurS)
for student in students:
    student.ShowStudentInfo()