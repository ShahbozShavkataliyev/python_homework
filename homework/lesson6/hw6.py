task 1

def modify_string(txt):
    vowels = "aeiou"
    i = 0
    result = ""

    while i < len(txt):
        result += txt[i]           
        if (i + 1) % 3 == 0:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i+1] == "_"):
                if i + 1 < len(txt) - 1:  
                    result += txt[i+1]    
                    result += "_"         
                    i += 1                
            else:
                if i != len(txt) - 1:      
                    result += "_"

        i += 1

    return result

print(modify_string("assalom"))

task 2 

n = int(input())

for i in range(n):
    print(i ** 2)

task 4

def non_common_elements(list1, list2):
    result = []

    for x in list1:
        if x not in list2:
            result.append(x)

    for x in list2:
        if x not in list1:
            result.append(x)

    return result




list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(non_common_elements(list1, list2))  
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(non_common_elements(list1, list2))  

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(non_common_elements(list1, list2))  
