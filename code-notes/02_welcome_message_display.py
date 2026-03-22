# Exercise 2 from Guanabara's Algorithm workbook!
# Write a program that reads a person's name and displays a welcome message: Ex: What is your name? John Smith Hello John Smith, it's a pleasure to meet you!

person_name = input("What is your name? ") 
print(f"Hello {person_name}, it's a pleasure to meet you!")

person_middle_name = input("Could you also tell me your middle name? ")
print(f"Hello {person_name} {person_middle_name}, it's a pleasure to meet you!")