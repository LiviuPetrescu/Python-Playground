import urllib.request, urllib.parse
import json, ssl

# Define API-ul
# Heavily rate limited proxy of https://www.geoapify.com/ api
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Ask for location
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    # Define a dict with "q" key and value received from the user
    address = address.strip()
    parms = dict()
    parms['q'] = address

    # Define API with parameters
    url = serviceurl + urllib.parse.urlencode(parms)
    #  The address from the test was Universidad de Valladolid
    # Retrieving https://py4e-data.dr-chuck.net/opengeo?q=Universidad+de+Valladolid
    # Retrieving https://py4e-data.dr-chuck.net/opengeo?q=Iasi+Romania
    print('Retrieving', url)

    # Open the URL and get the content (similar with file OPEN)
    uh = urllib.request.urlopen(url, context=ctx)

    # Save the answer in a variable after decoding it because it came from outside the application
    # The data at this moment are in a rougher form and still need processing
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))


    # Load the answer as JSON
    try:
        js = json.loads(data)
    except:
        js = None

    # Check if we got a dictionary with data and if in that data we have a dictionary with the key "features"
    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    # Check if dict has values
    if len(js['features']) == 0:
        print('==== Object not found ====')
        print(data)
        break

    # Save the variables that we are interested in (JSON-received from the other app)
    lat = js['features'][0]['properties']['lat']
    lon = js['features'][0]['properties']['lon']
    print('lat', lat, 'lon', lon)
    location = js['features'][0]['properties']['formatted']
    print(location)
    plus_code= lon = js['features'][0]['properties']["plus_code"]
    print(plus_code)