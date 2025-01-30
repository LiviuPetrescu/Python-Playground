# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# pentru request-urile  WEB folosim urllib /url OPEN
from urllib.request import urlopen
import soupsieve
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# DATA to enter: http://py4e-data.dr-chuck.net/known_by_Sarah.html
url = input('Enter - ')

# deschidem URL-ul si primim continutul
html = urlopen(url, context=ctx).read()

# folosim BeautifulSoup ca sa avem acces la intreaga pagina web asa cum este ea in format HTML
soup = BeautifulSoup(html, "html.parser")

# Acesta a fost un alt exercitiu
# # Retrieve all of the span tags
# span = soup("span")
# span_sum=0
# for s in span:
#     span_sum=span_sum+int(s.contents[0])
# print(span_sum)

# cautam si salvam toate ancorele e gresita exprimarea in variabilele de mai jos
tags = soup("a")
print("printam aconcorele:", tags)
counter_tags=0
loop_tags=0
seven_tag=""

# salvam valoarea acorei cu numarul 18
searched_tag =(tags[17].get('href'))

# dam click de 6 ori din link in link pana la link-ul 18 din utlima pagina
for element in range(6):
    if loop_tags==0:

        # Use it to make a secure HTTPS request context=ctx
        # variabila ctx este definita la inceputul scriptului
        # Secure Sockets Layer (SSL) is a protocol that was designed to provide security for communication over networks, particularly the internet.
        html = urlopen(searched_tag, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("a")
        seven_tag = (tags[17].get('href'))
    else:
            html = urlopen(seven_tag, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            tags = soup("a")
            seven_tag = (tags[17].get('href'))
    loop_tags=1

print(seven_tag)