TASK1

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(5)
print("Area:", c.area())
print("Perimeter:", c.perimeter())

TASK2

from datetime import date, datetime

class Person:
    def __init__(self, name, country, dob):  # dob = "YYYY-MM-DD"
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))


p = Person("John", "USA", "2000-05-10")
print("Age:", p.age())

TASK3

class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calc = Calculator()
print(calc.add(5, 3))

TASK4

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        import math
        return math.pi * self.r**2

    def perimeter(self):
        import math
        return 2 * math.pi * self.r


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return 4 * self.a


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        import math
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

TASK5

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(root, value):
            if root is None:
                return Node(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if root is None:
                return False
            if root.value == value:
                return True
            if value < root.value:
                return _search(root.left, value)
            return _search(root.right, value)
        
        return _search(self.root, value)

TASK6

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return "Stack is empty"

TASK8

class ShoppingCart:
    def __init__(self):
        self.items = {}  # item: price

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(self.items.values())



