# Cu diez putem adauga comentarii
"""
Sau cu aceasta metoda putem scrie pe mai multe
linii.
"""


"""
print('Hello World!')
txt = 'Hello World!'
print(txt[:12])
lista= [1,2,3]
for element in lista:
    print(element)
lista2 =[4]
lista2.append(5)
lista.extend(lista2)
print(lista)

lista_test=[1,2,3,4,5,6]
lista_test.pop(1)
# print(lista_test)
for element in range(len(lista_test)):
    print(lista_test[element])
lista_test.append(7)
lista_test.extend([7,8,9])
#print(lista_test)
lista_test.remove(7)
for index in range(0,5,2):
    print(lista_test[index])
for index in range(len(lista_test)):
    print(lista_test[index])
"""
# lista_text=["Ana", "are","mere","pere","banane","ciocolata"]
# lista_text[0:2].append("pere")
# print(lista_text)
# text_nou = lista_text[0]+" "+ lista_text[1]+" "+lista_text[3]
# print(text_nou)
#
# mylist = ['apple', 'banana', 'cherry']
# mylist[0] = 'kiwi'
# print(mylist)

# mylist = ['apple', 'banana', 'cherry']
# mylist[1:2] = ['kiwi', 'mango']
# print(mylist)
# mylist.insert(1,'lemon')
# print(mylist)
#
# fruits = ['apple', 'banana', 'cherry']
# newlist = [x for x in fruits if x == 'banana']
# print(newlist)
# fruits_2=list(fruits)
# print(fruits_2)

# x = 34
# y= 30
# produs= x*y
# suma = x+y
#
# if produs>1000:
#     print("Produsul este "+str(produs))
# else:
#     print("Suma este "+str(suma))

# Ruleaza un program care sa printeze primele 10 numere naturale si suma dintre numarul curent si numarul urmator

#
# for numar in range(1,11):
#     print(str(numar)+ " Numar")
#     suma = numar+numar+1
#     print(str(suma)+" Suma")
#     suma = 0

#printati numarul lipsa
# lista_test =[1,2,3,5,6,8,10]
# number_of_interations =0
# # for numar in range(len(lista_test)):
# #     print(str(numar)+" Index")
# while number_of_interations< len(lista_test)-1:
#     if lista_test[number_of_interations+1] -lista_test[number_of_interations] >1:
#         print(lista_test[number_of_interations]+1)
#     number_of_interations+=1

# string_excelent= "Excelent"
# for index in range(len(string_excelent)):
#     if index %2==1:
#         print(string_excelent[index])

# stergeti primele caractere din string
sterge_string =("Noi vrem sa invatam python si exersam stringurile")
string_sters=sterge_string[10:]
# print(string_sters)

#  printati True sau False daca primul element este egal cu ultimul
# lista_egale= [1,2,3,4,5,4]
#
#
# if lista_egale[0]==lista_egale[-1]:
#     print(True)
# else:
#     print(False)

#  lista elemente divizibile cu 5
# lista_1= [10,20,25,30,35]
# lista_2=[40,45,60,75,90]
# lista_3=[]
# for index in range(len(lista_1)):
#     if lista_1[index] %5==0:
#         lista_3.append(lista_1[index])
# for index in range(len(lista_2)):
#     if lista_2[index] %5==0:
#         lista_3.append(lista_2[index])
# print(lista_3)

lista_litere =["Ten","One","Zero"]
lista_cifre =[10,1,0]
dictionar_litere_cifre={}

# for key, values in dictionar_litere_cifre.items():
for caractere in range(len(lista_cifre)):
    dictionar_litere_cifre.update({lista_litere[caractere]: lista_cifre[caractere]})
# print(dictionar_litere_cifre)
dict_2 ={'Four': 4, 'Five': 5, 'Six': 6}
dict_3 ={}
for key, value in dictionar_litere_cifre.items():
    dict_3.update({key:value})
for key, value in dict_2.items():
    dict_3.update({key:value})
# print(dict_3)
sample_dict={
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }

}
# print(sample_dict["class"]["student"]["marks"]["history"])
# lista_test =[1,2,3,4,10]
# numar_min= lista_test[0]
# numar_max=lista_test[-1]
# for numere in range(1,numar_max+1):
#     if numere not in lista_test:
#         print("Numerul lipsa este "+str(numere))

# primele_numere=0
# lista_primele=[]
# while primele_numere <10:
#     lista_primele.append(primele_numere)
#     primele_numere+=1
# print(lista_primele)
#
# string_numere=[]
# for index in range(1,6):
#     string_numere.append(index)
#     print(string_numere)
#
# text_gol=""
# for index in range(1,6):
#     text_gol=text_gol+str(index)
#     print(text_gol)

# calculeaza suma de la 1 la numarul dat
# numar_dat=3
# suma=0
# for index in range(1,numar_dat+1):
#     suma=suma+index
# print(suma)

# filtrati lista cunumere divizibile cu  5 si mai mici decat 500
# numbers= [12,75,150,180,145,525,50]
# list_cinci =[]
# for element in numbers:
#     if element%5==0:
#         if element<500:
#             list_cinci.append(element)
#
# print(list_cinci)

numbers2=[3,6,15,150,30,900,1500,400]
numbers3=[]
# daca e divizibil cu 3 il afisez daca e mai mare de 500 break daca e mai 15 decat continuam
for elemente in numbers2:
    if elemente>500:
        break
    elif elemente %3==0:
        if elemente<15:
            continue
        numbers3.append(elemente)

# print(numbers3)
numar_mare =5698076
counter=0


while numar_mare !=0:
   numar_mare= numar_mare//10
   counter += 1

# print(counter)

# max_print=5
# while max_print>=1:
#     piramida=""
#     for index in range (max_print,0,-1):
#         piramida = piramida +" "+str(index)
#     max_print = max_print -1
#     print(piramida)

string_dat = 'La supermarket au mere, dar la piata au mere mai frumoase'
counter=0
string_transformat = string_dat.count("mere")
string_transformat_doi = string_dat.split()
for element in string_transformat_doi:
    if "mere" in element:
        counter+=1
# print(counter , "mere")
counter_doi=0
lungime_string= len(string_transformat_doi)
while lungime_string>0:
    if "mere" in string_transformat_doi[lungime_string-1]:
        counter_doi+=1
    lungime_string-=1

# print(counter_doi)