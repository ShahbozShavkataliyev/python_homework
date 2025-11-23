TASK2

n = int(input())

if n % 2 != 0 and n <= 20:
    print(f'{n} is weird')
elif n % 2 == 0 and n >= 2 and n <= 5:
    print(f"{n} is Not Weird")
elif n % 2 == 0 and  n >= 6 and n <= 20:
    print(f"{n} is Weird")
else:
    print(f"{n} is Not Weird")

TASK3

a = 5
b = 15


if a % 2 != 0:
    a += 1      
else:
    a = a       

evens = list(range(a, b + 1, 2))
print(evens)



a = 5
b = 15

first_even = a + (a % 2)   

evens = list(range(first_even, b + 1, 2))
print(evens)
