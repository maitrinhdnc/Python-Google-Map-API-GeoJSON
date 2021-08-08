from geojson import Feature, Point, FeatureCollection, dump
import requests, json

features = []

api = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&types={}&key={}'
latitude = 10.8007089
longitude = 106.6880843
radius = 2000
types = 'cafe'
api_key = 'AIzaSyCHl7srRpkpJc5n69gLWlbVCYGXsJn5lIQ'

ses = requests.Session()
resp = ses.get(api.format(latitude, longitude, radius, types, api_key))
data = json.loads(resp.text)
for d in data['results']:
    lat = d['geometry']['location']['lat']
    lng = d['geometry']['location']['lng']
    point = Point((lng, lat))
    addr = d['vicinity']
    name = d['name']
    features.append(Feature(geometry=point, properties={'name': name, 'address': addr}))

feature_collection = FeatureCollection(features)

with open('coffeenearme.geojson', 'w') as f:
   dump(feature_collection, f)