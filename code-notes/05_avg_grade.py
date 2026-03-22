# Exercise 5 from Guanabara's Algorithm workbook!
# Write a program that reads a student's two grades in a subject and displays their average grade for the subject on the screen. Example: Grade 1: 4.5 Grade 2: 8.5 The average between 4.5 and 8.5 is equal to 6.5

student_name = str(input("Enter the Student name: "))
student_MATHgrade = list(map(float, input("Enter the Student's grades for Math:").split(',')))
student_PTgrade = list(map(float, input("Enter the Student's grades for Portuguese:").split(',')))

averageMath = sum(student_MATHgrade) / len(student_MATHgrade)
averagePT = sum(student_PTgrade) / len(student_PTgrade)

print("Grade 1: ", student_MATHgrade[0], ", Grade 2: ", student_MATHgrade[1], "The average between ", student_MATHgrade[0], " and ", student_MATHgrade[1], " is equal to", averageMath)
print("Grade 1: ", student_PTgrade[0], ", Grade 2: ", student_PTgrade[1], "The average between ", student_PTgrade[0], " and ", student_PTgrade[1], " is equal to", averagePT)


# len() is a function that returns the number of items in a collection (like a list, string, or tuple). For example, len([1, 2, 3]) returns 3.
# list() converts things like map objects or other iterables into a list. For example, list(map(int, ["1", "2"])) gives [1, 2].

# So, to get the average grades we'll calculate using "sum" and "len". "sum(student_grade) / len(student_grade)" 
# "sum" will aggregate the values in student_grade, while len will give the number of the values in the grades that we entered. Ex: grades: 8, 7.5 -> 2 numbers -> 8 + 7.5 / 2 -> 15.5 / 2 -> 7.75.