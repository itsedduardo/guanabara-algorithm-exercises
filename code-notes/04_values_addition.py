# Exercise 4 from Guanabara's Algorithm workbook!
# Develop an algorithm that reads two integers and displays their sum. Example: Enter a value: 8 Enter another value: 5 The sum of 8 and 5 is equal to 13.

Value1 = int(input("Enter a value: "))
Value2 = int(input("Enter another value: "))

ValueSUM = Value1 + Value2 

print(f"The sum of {Value1} and {Value2} is equal to {ValueSUM}")

#Splitting ------------------------------

n1, n2 = map(int, input("Enter two numbers: ").split())
n3 = n1 + n2
print(f"There you have, the sum of {n1} and {n2} equals to {n3}")

# "split()" takes the user’s input (like "5 10") and splits it into a list of strings: ["5", "10"].
# "map(int, ...)" takes each string in that list and converts it to an integer, so you get [5, 10].