# Exercise 6 from Guanabara's Algorithm workbook!
# Write a program reads an integer and show it's predecessor and successor.

Userinput = int(input("insert a value: "))
p_Userinput = Userinput - 1
s_Userinput = Userinput + 1

print(f"Number: {Userinput}")
print(f"The predecessor of {Userinput} is: {p_Userinput}")
print(f"The successor of {Userinput} is: {s_Userinput}")