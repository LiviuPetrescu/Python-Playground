from Python_Scripts.First_Test import lungime_string

# lista_test= [1,2,3,4,5,6,10,20]
# print(lista_test[0])
# for element in lista_test:
#     print(element)
# for index in range(len(lista_test)):
#     print(lista_test[index])

lista_nume =["Ilinca", "Cristiana", "Rebeca", "Mara", "Adela","Mara", "Geo", "Mara"]
#for element in lista_nume:
    #print(element)

lista_nume.append("Mihai")
#print(lista_nume)
#lista_nume.sort()
#print(lista_nume)
#lista_nume.sort(reverse=True)
#print(lista_nume)
# print(lista_nume.index("Mara"))
# index_nume =[]
# print(lista_nume)
# for index in range(len(lista_nume)):
#     if lista_nume[index]== "Mara":
#         index_nume.append(index)
# print(index_nume)
# for element in lista_nume:
#     if element =="Mara":
#         lista_nume.remove(element)
# print(lista_nume)

palindrom= 121
verificare_palindrom=palindrom
# lista_rest=""
# ceva= palindrom %10
# while verificare_palindrom> 0:
#     rest=str(verificare_palindrom%10)
#     lista_rest=lista_rest+rest
#     verificare_palindrom=verificare_palindrom//10
# string_nou= int(lista_rest)
# if palindrom == string_nou:
#     print(True," Numarul este palindrom")
# else:
#     print(False)
# numar_intors=0
# while verificare_palindrom>0:
#     rest_imp=verificare_palindrom%10
#     numar_intors= (numar_intors*10) + rest_imp
#     print(numar_intors, "Numar intors")
#     print(rest_imp, " Rest Impartire")
#     verificare_palindrom=verificare_palindrom//10
# print(numar_intors)

#  creati un program care sa afiseze toate numerele prime de la 1 la 100
# lista_numere_prime=[]
# numar_prim=1
# lista_numere =[]
# for numar_natural in range(1,30):
#     print("Numarul curent este" ,numar_natural)
#     if numar_natural  ==numar_prim:
#         lista_numere_prime.append(numar_natural)
#         print("Am intrat in IF")
#     else:
#         lista_divizori=[]
#         for numere_prime in range(numar_prim+1,numar_natural):
#             print("Divizorul verificat este", numere_prime)
#             if numar_natural%numere_prime==0 :
#                 lista_divizori.append(numar_natural)
#                 break
#         if len(lista_divizori)==0:
#             print("Numarul este prim", numar_natural)
#             lista_numere_prime.append(numar_natural)
# print(lista_numere_prime)







primul_numar=1
# lista_prime=[]
# for numere_naturale in range(1,100):
#     if numere_naturale == primul_numar:
#         lista_prime.append(numere_naturale)
#     else:
#         lista_divizori=[]
#         for element in range(2,numere_naturale):
#             if numere_naturale%element==0:
#                 lista_divizori.append(element)
#                 break
#         if len(lista_divizori)==0:
#             lista_prime.append(numere_naturale)
#
# print(lista_prime)


string_intreg="Python"
lungime=int(len(string_intreg))
jumatate=int(lungime/2)
print(jumatate)
string_compus=string_intreg[0]+string_intreg[jumatate-1]+string_intreg[lungime_string-1]
print(string_compus)

# def parsare_string(input_string):
#     lungime = int(len(input_string))
#     jumatate = int(lungime / 2)
#     substring = input_string[0] + input_string[jumatate ] + input_string[lungime_string - 1]
#     return substring
# teat_opt=parsare_string("Liviu")
# print(teat_opt)

# string_dat="Astazi este Miercuri si este innorat"
# lista_cuvinte=string_dat.split()
# print(len(lista_cuvinte))
# dictionar_nou={}
# lista_chei=[]
# lista_valori=[]
# for element in range(len(lista_cuvinte)):
#     if element % 2 ==0:
#         lista_chei.append(lista_cuvinte[element])
#     else:
#         lista_valori.append(lista_cuvinte[element])
#
# for elemente in range(len(lista_chei)):
#     dictionar_nou.update({lista_chei[elemente]:lista_valori[elemente]})
#
# print(dictionar_nou)
# dictionar_modern={}
# for index in range(0,len(lista_cuvinte),2):
#     dictionar_modern.update({lista_cuvinte[index]:lista_cuvinte[index+1]})
# print(dictionar_modern)


x = 12
if x < 5:
    print("smaller")
else:
    print("bigger")
print("all done")












