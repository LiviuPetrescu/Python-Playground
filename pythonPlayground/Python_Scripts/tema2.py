from itertools import count

empty_list =[]
for index in range(1,11):
    empty_list.append(index)
correct_list= empty_list
print(correct_list)
suma = sum(correct_list)
print(suma)
lista_string =["Ana", "Geo", "Mihai"]
lista_string.append("Mihnea")
print(lista_string)
print(len(lista_string))
string_tema ="Mama are mere, cate mere are mama?"

lista_string_tema= string_tema.split()
print(lista_string_tema)
print(type(lista_string_tema))


lista_stringuri =[]
mix_lista =["Ana",20, 2.0]
for element in mix_lista:
    lista_stringuri.append(str(element))
print(lista_stringuri)
companie = "Abbot"
numar_litere =len(companie)
print(numar_litere)
vacanta= "Weekend placut!"
lungime_vacanta = len(vacanta)
jumatate_lungime = int(lungime_vacanta/2)
print(jumatate_lungime)
mijloc_lista=[]
for index in range(len(vacanta)):
    if index == jumatate_lungime -1 or index == jumatate_lungime or index ==jumatate_lungime+1:
        mijloc_lista.append(vacanta[index])
print(mijloc_lista)
print(vacanta[jumatate_lungime-1:jumatate_lungime+2])

