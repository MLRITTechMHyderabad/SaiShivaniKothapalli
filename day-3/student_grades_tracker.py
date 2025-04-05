n = int(input("Enter no. of students: "))
students = {} 
for i in range(n):
    name = input("Enter student name: ")
    grades = list(map(int, input("Enter grades: ").split()))
    students[name] = grades
    average = {name: sum(grades) / len(grades) for name, grades in students.items()}
    highest_avg = max(average, key=average.get)
    N = sum(1 for avg in average.values() if avg >= 50)
print("Student Grades:", students)
print("Average of Grades:", average)
print("Highest Average:", highest_avg)
print("Number of Students Passed:", N)






