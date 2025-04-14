
from datetime import datetime, timedelta
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe,RecipeHistory
from .forms import RecipeForm

@login_required
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user  
            recipe.save()
            messages.success(request, "Recipe added successfully!")
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "recipes/form.html", {"form": form, "title": "Add Recipe"})



@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            updated_recipe = form.save(commit=False)
            # updated_recipe.name = recipe.name  
            updated_recipe.save()
            messages.success(request, "Recipe updated successfully!")
            return redirect("recipe_detail", recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, "recipes/form.html", {"form": form, "title": "Edit Recipe", "recipe": recipe})



@login_required
def recipe_list(request):
    recipes = Recipe.objects.filter(user=request.user,active=True)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, "recipes/recipe_detail.html", {"recipe": recipe})


@login_required
def recipe_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.active=False
    recipe.save()
    messages.success(request, "Recipe deleted successfully!")
    return redirect("recipe_list")


@login_required
def mark_as_made(request, id):
    recipe = get_object_or_404(Recipe, id=id)  # Fetch the recipe
    
    already_made = RecipeHistory.objects.filter(
        user=request.user, recipe=recipe, made_on=datetime.now().date()
    ).exists()
    
    if already_made:
        messages.warning(request, "You have already marked this recipe as made today!")
        return redirect('recipe_detail', recipe_id=id)
    else:
        RecipeHistory.objects.create(user=request.user, recipe=recipe)
        messages.success(request, "Recipe marked as made today!")
        return redirect('recipe_list')

@login_required
def recipe_history(request):
    history = RecipeHistory.objects.filter(user=request.user).order_by("-made_on")
    return render(request, "recipes/recipe_history.html", {"history": history})



@login_required
def suggest_random_recipe(request):
    user_id = request.user.id
    five_days_ago = datetime.now().date() - timedelta(days=5)

    recent_recipes = RecipeHistory.objects.filter(
        user_id=user_id, made_on__gte=five_days_ago
    ).values_list("recipe_id", flat=True)

    available_recipes = Recipe.objects.exclude(id__in=recent_recipes).filter(
        source_link__isnull=False, source_link__exact=''
    ).exclude(source_link='') 

    if available_recipes.exists():
        random_recipe = random.choice(list(available_recipes))
        return render(request, "recipes/random_recipe.html", {"recipe": random_recipe})
    else:
        messages.warning(request, "No new recipes with source link found in the last 5 days!")
        return render(request, "recipes/random_recipe.html", {"recipe": None})


@login_required
def suggest_user_random_recipe(request):
    user_id = request.user.id
    five_days_ago = datetime.now().date() - timedelta(days=5)

    recent_recipes = RecipeHistory.objects.filter(
        user_id=user_id, made_on__gte=five_days_ago
    ).values_list("recipe_id", flat=True)

    user_recipes = Recipe.objects.filter(user=request.user).exclude(id__in=recent_recipes)

    if user_recipes.exists():
        random_recipe = random.choice(list(user_recipes))
        return render(request, "recipes/random_recipe.html", {"recipe": random_recipe})
    else:
        messages.warning(request, "You've already made all your recipes in the last 5 days!")
        return render(request, "recipes/random_recipe.html", {"recipe": None})



@login_required
def veg_recipes(request):
    recipes = Recipe.objects.filter(user=request.user, Mode="V", active=True)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "title": "Veg Recipes"})

@login_required
def non_veg_recipes(request):
    recipes = Recipe.objects.filter(user=request.user, Mode="N", active=True)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "title": "Non-Veg Recipes"})

@login_required
def breakfast_recipes(request):
    recipes = Recipe.objects.filter(user=request.user, category="B", active=True)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "title": "Breakfast Recipes"})

@login_required
def lunch_recipes(request):
    recipes = Recipe.objects.filter(user=request.user, category="L", active=True)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "title": "Lunch Recipes"})

@login_required
def dinner_recipes(request):
    recipes = Recipe.objects.filter(user=request.user, category="D", active=True)
    return render(request, "recipes/recipe_list.html", {"recipes": recipes, "title": "Dinner Recipes"})
