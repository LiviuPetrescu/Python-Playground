import datetime
def nume_varsta(nume,varsta):
    penume=nume
    ani=varsta
    mesaj="Numele meu este ",penume, " si am ",ani, " de ani"
    return mesaj
prezentare = nume_varsta("Liviu", 37)
print(prezentare)

def calculeaza_suma(*operatori):
    suma=0
    for element in operatori:
        suma=suma+element
    return suma
primul_test=calculeaza_suma(20,40,60)
print(primul_test)

# Exercise 3: Return multiple values from a function
def calculeaza(a,b):
    suma="Suma celor numere este ", a+b
    diferenta ="Diferenta celor doua numere este ",a-b
    return suma,diferenta
test_doi=calculeaza(30,20)
print(test_doi)

# Exercise 4: Create a function with a default argument
# Write a program to create a function show_employee() using the following conditions.
#
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def salary_name(name, salary=9000):
#     return name,salary
#
# testul_trei=salary_name("Liviu")
# print(testul_trei)
# testul_patru = salary_name("Elena", 8000)
# print(testul_patru)

# Outer/Inner function

# outer function
def outer_fun(a, b):

    # inner function
    def addition(b, c):
        return b + c

    # call inner function from outer function
    add = addition(a, b)
    # add 5 to the result
    return add + 5

result = outer_fun(5, 10)
print(result)

# Create a recursive function
def addition(num):
    if num:
        # call same function by reducing number by 1
        print(num)
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)

# print(list(range(4, 30, 2)))

# Exercise 9: Find the largest item from a given list
lista_data=[4,8,30,2,11]
numar_maxim=lista_data[0]

for element in lista_data:
    if element>numar_maxim:
        numar_maxim=element
print("Aici", numar_maxim)
print(max(lista_data))
str1 = "JaSonAy"
lungime_str=len(str1)
mijloc=int(lungime_str/2)
string_mijloc=str1[mijloc-1]+str1[mijloc]+str1[mijloc+1]
print(string_mijloc)
# use string slicing to get result characters
res = str1[mijloc - 1:mijloc + 2]
print(res)


def get_middle_three_chars(str1):
    print("Original String is", str1)

    # first get middle index number
    mi = int(len(str1) / 2)

    # use string slicing to get result characters
    res = str1[mi - 1:mi + 2]
    print("Middle three chars are:", res)

get_middle_three_chars("JhonDipPeta")
get_middle_three_chars("JaSonAy")


s1 = "Ault"
s2 = "Kelly"
def play_function(str2,str3):
    mijloc_play=int(len(str2)/2)
    str4= str2[mijloc_play:len(str2)]
    str4= str3+str4
    str4= str2[:mijloc_play]+str4
    return str4
check_play= play_function(s1,s2)
print(check_play)

str1 = "PyNaTive"
str2=str1.lower()
str3=""
str4=''
for index in range(len(str1)):
    if str1[index]!=str2[index]:
        str3= str3+str1[index]
    else:
        str4=str4+str1[index]
    print(str3)
    print(str4)
str3=str4+str3
print(str3)

#  Varianta2
str1 = "PYnAtivE"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)

# Numara caractere,numere, simboluri
chars = 0
digits = 0
symbol = 0
str1 = "P@#yn26at^&i5ve"
for element in str1:
    if element.isdigit():
        digits=digits+1
    elif element.isalpha():
        chars=chars+1
    else:
        symbol=symbol+1
print(digits,chars, symbol)

str1 = "Apple"
dict={}
for element in str1:
    dict.update({element:str1.count(element)})
print(dict)


#  Varianta 2
# create a result dictionary
# char_dict = dict()
#
# for char in str1:
#     count = str1.count(char)
#     # add / update the count of a character
#     char_dict[char] = count
# print('Result:', char_dict)

# str1 = "PYnative"
# str1 = ''.join(reversed(str1))
# print("Reversed String is:", str1)
#
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#
# # use built-in function filter to filter empty value
# new_str_list = list(filter(None, str_list))
#
# print("After removing empty strings")
# print(new_str_list)

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
res=[]
for index in range(len(l1)):
    if index%2==1:
        l3.append(l1[index])
    else:
        l3.append(l2[index])
print(l3)

odd_elements = l1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = l2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

#  Seturi
# result = zip(first_list, second_list)
# result_set = set(result)
# print(result_set)
# print(result_set)
# book_set = set(("Harry Potter", "Angels and Demons", "Atlas Shrugged"))
# print(book_set)
# output {'Harry Potter', 'Atlas Shrugged', 'Angels and Demons'

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# print("First Set ", first_set)
# print("Second Set ", second_set)
#
# intersection = first_set.intersection(second_set)
# print("Intersection is ", intersection)
# for item in intersection:
#     first_set.remove(item)
#
# print("First Set after removing common element ", first_set)


# Exercise 8: Iterate a given list and check if a given element
# exists as a key’s value in a dictionary. If not, delete it from the list

# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# new_list=[]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
# for element_lista in roll_number:
#     if element_lista in sample_dict.values():
#         print("Lista IF",element_lista)
#         new_list.append(element_lista)
#
# roll_number=new_list
# print(roll_number)

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original list", sample_list)

sample_list = set(sample_list)
print("unique list", sample_list)
print(max(sample_list))

list1 = [100, 200, 300, 400, 500]
# list1.reverse()

print(list1[len(list1)::-1])

# tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# print(tuple1[1][1])
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple2)
# print(tuple1)

# Print date and time
print(datetime.datetime.now())

# only time
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())