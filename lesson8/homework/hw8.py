TASK1

try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

TASK2

try:
    x = input("Enter an integer: ")
    x = int(x)  
    print("You entered:", x)
except ValueError:
    print("Error: That is not a valid integer!")

TASK3

try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError:
    print("Error: File does not exist!")

TASK4

try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numeric!")

    a = float(a)
    b = float(b)
    print(a + b)
except TypeError as e:
    print("Error:", e)

TASK5

try:
    file = open("/root/secret.txt", "r")  # Restricted path
except PermissionError:
    print("Error: You do not have permission to access this file!")

TASK6

my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range!")

TASK7

try:
    x = input("Enter a number: ")
    print("You entered:", x)
except KeyboardInterrupt:
    print("\nInput cancelled by user!")

TASK8

try:
    result = 10 / 0  
except ArithmeticError:
    print("Arithmetic error occurred!")

TASK9

try:
    file = open("data.txt", "r", encoding="ascii")
    content = file.read()
except UnicodeDecodeError:
    print("Error: Encoding issue! File contains non-ASCII characters.")

TASK10

my_list = [1, 2, 3]

try:
    my_list.push(4)  
except AttributeError:
    print("Error: List object has no such attribute!")


