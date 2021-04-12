
import json
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'proj.settings'
#NOTE: PROJECT NAME SHOULD BE DIFFERENT TO ROOT DIRECTORY OTHERWISE MODULE ERROR
django.setup()
from ingredientsApp.models import Recipe, Category

path_to_json = 'data/full_format_recipes.json'


with open(path_to_json, 'r') as f:
    data = json.load(f)
    for i, entry in enumerate(data):
        #print(entry)
        r = Recipe(id=i)
        print("ok")
        
        print("good")
        r.name = str(entry['title'])
        r.desc = entry['desc']
        r.directions = entry['directions']
        r.fats = int(entry['fat'])
        r.calories = int(entry['calories'])
        r.protein = int(entry['protein'])
        r.sodium = int(entry['sodium'])
        r.ingredDetails = entry['ingredients']
        for c in entry['categories']:
            r.categories.create(name=str(c))
        print(i)

