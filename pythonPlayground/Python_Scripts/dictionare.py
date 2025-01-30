# thisdict = {
#   "brand": ["Ford","Dacia","Opel"],
#   "model": ["Mustang","Sandero"],
#   "year": [1964]
# }
# # for element_dict in thisdict:
# #     print(element_dict)
#
# # "for key, value in thisdict.items():
# #      print(key)
# #      print(value)"
#
# for key, value in thisdict.items():
#     if len(value)==3:
#         print(key)

dictionar_pare_impare ={}
lista_pare=[]
lista_impare=[]
for index in range(1,21):
    if index %2==0:
        lista_pare.append(index)
    else:
        lista_impare.append(index)
print(lista_pare)
print(lista_impare,"impare")
for element in range (0,10):
    dictionar_pare_impare.update({lista_impare[element]:lista_pare[element]})
print(dictionar_pare_impare)


