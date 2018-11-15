import json
import os

with open('Data.json') as f:
    data = json.load(f)
    for p in data['people']:
        print(p['name'])
        for car in p['cars']:
            print(car['name'])

print("-----")
print(data['people'][1]['cars'][0]['name'])

test = data['people'][0]['name']

if test == 'Scott':
    with open('data.json', 'w') as outfile:
        data['people'][0]['name'] = 'Ben'
        json.dump(data, outfile, indent=4)

else:
    with open('data.json', 'w') as outfile:
        data['people'][0]['name'] = 'Scott'
        json.dump(data, outfile, indent=4)

print("-----")
print(data['people'][0]['name'])
print("-----")

if os.path.isfile('./data.json') == True:
    print('true')