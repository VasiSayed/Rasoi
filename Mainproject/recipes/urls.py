from django.urls import path
from .views import recipe_list, recipe_detail, recipe_create, recipe_delete,recipe_history,mark_as_made,suggest_random_recipe,suggest_user_random_recipe
from .views import veg_recipes,non_veg_recipes,breakfast_recipes,lunch_recipes,dinner_recipes,recipe_edit
urlpatterns = [
    path("", recipe_list, name="recipe_list"),
    path("recipe/<int:recipe_id>/", recipe_detail, name="recipe_detail"),
    path("recipe/add/", recipe_create, name="recipe_create"),
    path("recipe/<int:recipe_id>/delete/", recipe_delete, name="recipe_delete"),
    path('mark-recipe/<int:id>/',mark_as_made,name='Markas'),
    path("history/", recipe_history, name="recipe_history"),
    path("suggest-recipe/", suggest_random_recipe, name="suggest_random_recipe"),
    path('my-random/', suggest_user_random_recipe, name='suggest_user_random_recipe'),
    path("recipes/veg/", veg_recipes, name="veg_recipes"),
    path("recipes/non-veg/", non_veg_recipes, name="non_veg_recipes"),
    path("recipes/breakfast/", breakfast_recipes, name="breakfast_recipes"),
    path("recipes/lunch/", lunch_recipes, name="lunch_recipes"),
    path("recipes/dinner/", dinner_recipes, name="dinner_recipes"),
    path('recipe/<int:recipe_id>/edit/', recipe_edit, name='recipe_edit'),
]
