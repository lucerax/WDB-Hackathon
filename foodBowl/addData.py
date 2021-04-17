
import json
import os
import django
os.environ["DJANGO_SETTINGS_MODULE"] = 'proj.settings'
#NOTE: PROJECT NAME SHOULD BE DIFFERENT TO ROOT DIRECTORY OTHERWISE MODULE ERROR
django.setup()
from ingredientsApp.models import Recipe, Category

path_to_json = 'data/full_format_recipes.json'

def get_id():
    i = 0
    while True:
        yield i
        i+=1
        
        
a = get_id()

with open(path_to_json, 'r') as f:
    data = json.load(f)
    for i, entry in enumerate(data):
        print(entry)
        r = Recipe(id=i)
        r.name = str(entry['title'])
        r.desc = str(entry['desc'])
        r.directions = entry['directions']
        if entry['fat']:
            r.fats = entry['fat']
        if entry['calories']:
            r.calories = int(entry['calories']) 
        
        if entry['protein']:
            r.protein = int(entry['protein'])  
        
        if entry['sodium']:
            r.sodium = int(entry['sodium']) 

        r.ingredDetails = entry['ingredients']
        r.save()

        for c in entry['categories']:
            cat = Category(id = next(a))
            #cat.save()
            r.categories.add(i)

        print(i)
        r.save()

