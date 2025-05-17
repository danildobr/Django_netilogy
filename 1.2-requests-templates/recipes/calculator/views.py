from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def get_recipe(request, dish_name):
    if dish_name not in DATA:
        return render(request, 'calculator/index.html', {'recipe':{}})
                
    servings = int(request.GET.get('servings', 1))
    print(DATA[dish_name])
    recipe = {ingredient: amount * servings 
             for ingredient, amount in DATA[dish_name].items()}
    
    return render(request, 'calculator/index.html', {'recipe': recipe})


def omlet(request):
    return get_recipe(request, 'omlet')

def pasta(request):
    return get_recipe(request, 'pasta')

def buter(request):
    return get_recipe(request, 'buter')