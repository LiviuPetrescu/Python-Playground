import urllib.request
import xml.etree.ElementTree as ET

"""
In this script Element Tree is used to manipulate XML content
"""


url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2149159.xml '

print('Retrieving', url)

# Open URL-ul
uh = urllib.request.urlopen(url)

#  Read the data(entire XML document)
data = uh.read()
print("print data:", data)
print('Retrieved',len(data),'characters')

# 'tree' is an object from XML element tree class
tree = ET.fromstring(data)

# Save in a list all attributes with "count" name
counts = tree.findall('.//count')
nums = list()

# Iterate through the list and cast "count" as int
for result in counts:
    nums.append(int(result.text))
print('Count:', len(nums))
print('Sum:', sum(nums))
