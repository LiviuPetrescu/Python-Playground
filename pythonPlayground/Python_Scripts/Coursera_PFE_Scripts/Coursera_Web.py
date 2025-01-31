from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

"""
In this script BeautifulSoup is used to have access to the entire web page as it is in HTML format
"""


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# DATA to enter: http://py4e-data.dr-chuck.net/known_by_Sarah.html
url = input('Enter - ')

# Get URL and read the content
html = urlopen(url, context=ctx).read()

# We use BeautifulSoup to have access to the entire web page as it is in HTML format
soup = BeautifulSoup(html, "html.parser")


# Search and save all the anchors
anchors = soup("a")
print("print anchors:", anchors)
counter_anchors=0
loop_anchors=0
seven_anchor= ""

# Get the wanted anchor
searched_anchor =(anchors[17].get('href'))

# Click six times from link to link
for element in range(6):
    if loop_anchors==0:

        # Use it to make a secure HTTPS request context=ctx
        # ctx variable is defined at the beginning of the script
        # Secure Sockets Layer (SSL) is a protocol that was designed to provide security for communication over networks, particularly the internet.
        html = urlopen(searched_anchor, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        anchors = soup("a")
        seven_anchor = (anchors[17].get('href'))
    else:
            html = urlopen(seven_anchor, context=ctx).read()
            soup = BeautifulSoup(html, "html.parser")
            anchors = soup("a")
            seven_anchor = (anchors[17].get('href'))
    loop_anchors=1

print(seven_anchor)