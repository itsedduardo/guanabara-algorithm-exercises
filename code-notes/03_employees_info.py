# Exercise 3 from Guanabara's Algorithm workbook!
# Write a program that reads an employee's name and salary, displaying a message at the end. Example: Employee Name: Maria do Carmo Salary: 1850.45 The employee Maria do Carmo has a salary of R$1850.45 in June.

Employee_name = str(input("What is the employer's name? "))
Employee_Salary = float(input("What is the Employer's salary? "))

print("---------------")
print(f"Employee name: {Employee_name}")
print(f"{Employee_name}'s Salary: {Employee_Salary}")
print(f"The employee from or corporate, {Employee_name} has a salary of R${Employee_Salary} in June 2025")
print("---------------")

# The "f" in the "print(f"...")" indicates a formatted string. It allows you to embed expressions inside curly braces "{}" within the string. their are evaluated at runtime and replaced with their's stated values.