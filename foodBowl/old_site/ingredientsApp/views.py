  
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Recipe
import json
from django.views.decorators.csrf import csrf_exempt
import re

def categoryView(request):
    allCategories = Category.objects.all()
    return render(request, 'ingredient.html', {'allCategories': allCategories})


def recipeSearch(request, categoryID):
    """
    This is the functional view for search recipe page. Initially displays all recipes unfiltered.
    Matches single category
    """
    allRecipes = Recipe.objects.all() #obtains all objects of class type recipe
    categoryObject = Category.objects.get(id = categoryID) #makes a query
    payload = []
    listRecipes = []

    for i, curRecipe in enumerate(allRecipes):
        names = []
        recipeCategories = curRecipe.categories.all() #gets all category tags for the recipe
        
        #TODO: possibly precompute these categories
        for category in recipeCategories:
            names.append(category.name)

        #print("TYPE OF DIRS IS:", type(curRecipe.directions))
        dirs = re.findall("'(.*?)'", curRecipe.directions)
        #print(curRecipe.directions)
        # for d in dirs:
        #     print(d)

        ingreds = re.findall("'(.*?)'", curRecipe.ingredDetails)

        if set(payload).issubset(set(names)):
            listRecipes.append({'name': curRecipe.name,
            'ingredients': ingreds,  #list of details
            'directions': dirs, #list of steps
            'calories': curRecipe.calories,
            'protein': curRecipe.protein,
            'fats': curRecipe.fats, 
            'sodium': curRecipe.sodium})

    return render(request, 'searchRecipe.html',
    {'categoryObject': categoryObject,
    'allRecipes': allRecipes,
    'listRecipes' : listRecipes})


def getCategoryID(request, categoryName):
    """
    Since we have a many to many relation between categories (like apple, bacon, dinner, vegetarian) and recipes
    we need to access by ID for querying. This method gets the category ID.
    """
    if request.method == 'GET':
        try:
            categoryID = Category.objects.get(name = categoryName).id
            response = json.dumps([{'categoryId': categoryId}])
        except:
            response = json.dumps([{'Error': 'No ID with that name'}])

        return HttpResponse(response, content_type='text/json')

#get match recipes by list of ingredients
@csrf_exempt
def getMatchRecipe(request):
    """
    Gets matching recipes based on post request with a list of categories

    """
    if request.method == 'POST':
        payload = json.loads(request.body).get('listCategories') #TODO: CHECK
        try:
            allRecipes = Recipe.objects.all()
            response = []
            for i in range(0, len(allRecipes)):
                names = []
                categories = allRecipes[i].categories.all()
                for j in range(0, len(categories)):
                    names.append(categories[j].name)

                if set(payload).issubset(set(names)):
                    curRecipe = allRecipes[i]
                    response.append({'name': curRecipe.name,
                    'ingredients': curRecipe.ingredDetails,  #list of details
                    'directions': curRecipe.directions, #list of steps
                    'calories': curRecipe.calories,
                    'protein': curRecipe.protein,
                    'fats': curRecipe.fats, 
                    'sodium': curRecipe.sodium})
            response = json.dumps(response)
        except:
            response = json.dumps([{'Error': 'No id with that name'}])
    else:
        response = json.dumps(["HELLO"])
    return HttpResponse(response, content_type='text/json')