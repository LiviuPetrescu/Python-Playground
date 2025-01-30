#  Exercitiul 2
# suma=0
# for index in range(10):
#     if index==0:
#         print(suma)
#     else:
#         suma=index+index-1
#         print(suma)
# #  Exercitiul 3
# input_string=input("Va rog introduceti un cuvant")
# str="PYnative"
# for index in range (len(input_string)):
#     if index%2==0:
#         print(input_string[index])
from Python_Scripts.Exercises import index
from Python_Scripts.First_Test import numbers2
from Python_Scripts.Numere_prime_Fibonacci import lista_prime

# Exercise 4: Remove first n characters from a string
# remove_chars("PYnative", 4)
# given_string="PYnative"
# def remove_chars(input_string,number_of_chars):
#     given_string = input_string
#     partial_string =given_string[number_of_chars:]
#     # for index in range (number_of_chars,len(given_string)):
#     #     partial_string = partial_string+given_string[index]
#     return partial_string
# pice_of_string=remove_chars("PYnative",2)
# print(pice_of_string)

# patern_list=[1,2,3,4,5]
#
# for element in patern_list:
#     string_gol = ''
#     for print_time in range(element):
#         string_gol=string_gol+str(element)+" "
#     print(string_gol)

# numar= 789878
# string_numar=str(numar)
# lista_numar=[]
# for element in string_numar:
#     lista_numar.append(element)
# print(lista_numar)
# string_intermediar=""
# for index in range(len(lista_numar)-1,-1,-1):
#     string_intermediar=string_intermediar+lista_numar[index]
#
# print(int(string_intermediar))

# Calculator impozit
#  pe 10000 trebuie sa fie 0
#  pe 10000 trebuie sa fie 10%
# first_part = 10000
# second_part = 20000
# venit_total = 45000
# impozit = 0
# if venit_total<first_part:
#     impozit = 0
# elif venit_total<second_part:
#     diferenta = venit_total-first_part
#     impozit = diferenta*0.1
# else:
#     impozit = first_part*0.1
#     impozit = impozit+(venit_total-second_part)*0.2
# print(impozit)

# Exercise 13: Print multiplication table from 1 to 10
# lista_numere=[]
# for index in range(1,11):
#     for second_index in range(1,11):
#         number= index*second_index
#         lista_numere.append(number)
# print(lista_numere)
#
# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

# def exponent(base, exp):
#     iterator = exp
#     result = 1
#     while iterator > 0:
#         result = result * base
#         print(result)
#         iterator = iterator - 1
#     print(base, "raises to the power of", exp, "is: ", result)
#
# exponent(5, 4)

# Exercise 1: Accept numbers from a user
# primul_nr=input("primul numar")
# al_doilea_nu=input("al doliea numar")
# produs=int(primul_nr)*int(al_doilea_nu)
# print(produs)

# print('My', 'Name', 'Is', 'James', sep='-')

# Exercise 5: Display numbers from a list using a loop
numbers = [12, 75, 150, 180, 145, 525, 50]
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop

# for element in numbers:
#     if element>500:
#         break
#     else:
#         if element % 5 == 0:
#             if element > 150:
#                 continue
#             else:
#                 print(element)

test_number=8970

# counter=0
# while test_number != 0:
#     test_number = test_number // 10
#     counter= counter+1
#     print(test_number)
# print(counter)
# counter_py=5
# while counter_py>0:
#     for index in range(counter_py, 0, -1):
#         print(index,end=' ')
#     counter_py=counter_py-1

# printeaza lista invers
# lista=[1,2,3,4,5,6]
# lista_invers=reversed(lista)
# for element in lista_invers:
#     print(element)
# for index_negativ in range(10,0,-1):
#     print(-index_negativ)

# Exercise 13: Find the factorial of a given number
# produs=1
# for index_factorial in range(5,1,-1):
#     produs=produs*index_factorial
# print("produs ",produs)

# Cubul
# for cub in range(1,7):
#     print(cub," Cubul este", cub*cub*cub)

# Exercise 17: Find the sum of the series up to n terms
string_dublu=""
numar_dat="2"
suma=0
for element in range(5):
    string_dublu=string_dublu+numar_dat
    suma=suma+int(string_dublu)
print(suma)

# n = 5
# # first number of sequence
# start = 2
# sum_seq = 0
#
# # run loop n times
# for i in range(0, n):
#     sum_seq += start
#     # calculate the next term
#     start = start * 10 + 2
# print("\nSum of above series is:", sum_seq)

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")


import json

data = {"key1" : "value1", "key2" : "value2"}

jsonData = json.dumps(data)
print(jsonData)


