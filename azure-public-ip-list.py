import json
with open('ServiceTags_Public_20211129.json', 'r') as f:
    data = json.load(f)

for element in data['values']:
    region_id = element['properties']['regionId']
    if 0 < region_id < 1000:
        print(element['properties']['addressPrefixes'])