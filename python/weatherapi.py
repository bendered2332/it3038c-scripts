import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http: // api.openweathermap.org/data/2.5/weather?zip=%s,appid=cc61dc9c38c39e2edc0627ac1d2c54a2' % zip)
data = r.json()

print("The weather in %s is %s" % (zip, data['weather'][0]['description']))
