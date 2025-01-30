start = 1
end = 30
print("Prime numbers between", start, "and", end, "are:")

lista_prime=[]
for numere_naturale in range(start,end):
    if numere_naturale == start:
        lista_prime.append(numere_naturale)
    else:
        lista_divizori=[]
        for element in range(2,numere_naturale):
            if numere_naturale%element==0:
                lista_divizori.append(element)
                break
        if len(lista_divizori)==0:
            lista_prime.append(numere_naturale)

print(lista_prime)

# Run the loop 10 times
# In each iteration
# print num1 as the current number of the sequence
# Add the last two numbers to get the following number result = num1 + num2
# update values of num1 and num2. Set num1 = num2 and num2 = result
num1=0
num2=1

for element in range(1,11):
    print(num1)
    result = num1 + num2
    num1 = num2
    num2 = result