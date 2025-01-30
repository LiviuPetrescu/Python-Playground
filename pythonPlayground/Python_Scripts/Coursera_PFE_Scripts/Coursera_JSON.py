import json
import urllib.request


url = input('Enter location: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2149160.json '
print('Retrieving', url)

# Open the URL and get the content
uh = urllib.request.urlopen(url)

#  Assign the answer to a variable (this contains also new line \n and other values)
data = uh.read()

#  Load as JSON format
info = json.loads(data)

specific_info=info["comments"]
print("Print Info: ",specific_info)
numbers=[]
for ele in specific_info:
    numbers.append(ele["count"])
print(sum(numbers))
