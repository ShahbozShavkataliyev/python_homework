TASK1

data = {"a": 5, "b": 2, "c": 9, "d": 1}

sorted_list = sorted(data.values())

sorted_list


data = {"a": 5, "b": 2, "c": 9, "d": 1}

sorted_data = sorted(data.values(),reverse = True)

sorted_data

TASK2

num_dict = {0: 10, 1: 20}

num_dict.update([(2,30)])

num_dict

TASK3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic1.update(dic2)

dic1.update(dic3)

dic1

TASK4

n = 5
result = {}

for x in range(1, n + 1):
    result[x] = x * x

print(result)

TASK5

n = 15
result = {}

for x in range(1, n + 1):
    result[x] = x * x

print(result)

TASK1

my_set = {1,2,2,3,5,6,'hello','world'}

print(my_set)

TASK2

sets = {'banana','apple','peach','banana'}

for val in sets:
    print(val)

TASK3

sets = {'banana','apple','peach','banana'}

sets.add('orange')

print(sets)

TASK4

my_set = {1,2,2,3,5,6,'hello','world'}

my_set.remove(2)

my_set

TASK5

my_set = {1,2,2,3,5,6,'hello','world'}

my_set.discard(2)

my_set


