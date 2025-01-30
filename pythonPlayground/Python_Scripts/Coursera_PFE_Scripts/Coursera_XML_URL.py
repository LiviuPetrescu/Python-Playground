import urllib.request
import xml.etree.ElementTree as ET

#  folosim Element Tree pentru a utiliza datele returnate de XML
#  folosim urllib request ca la oricare alt tip de adresa

url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2149159.xml '

print('Retrieving', url)

# deschidem URL-ul
uh = urllib.request.urlopen(url)

#  citim raspunsul intr-o forma mai bruta (intreg continultul documentului XML)
data = uh.read()
print("PRINTEZ DATA:", data)
print('Retrieved',len(data),'characters')

# tree este un obiect din clasa xml element tree
tree = ET.fromstring(data)

# salvam intr-o lista toate atributele cu numele "count"
counts = tree.findall('.//count')
nums = list()

# parcurgem lista si convertim textul din atributul "count" in int
for result in counts:
    # Debug print the data :)
    nums.append(int(result.text))
print('Count:', len(nums))
print('Sum:', sum(nums))
