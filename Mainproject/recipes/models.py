from django.db import models
from accounts.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Fixed comma issue
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="recipes/", blank=True, null=True)
    ingredients = models.TextField(blank=True,null=True)  
    source_link = models.URLField(blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    Mode=models.CharField(max_length=20,choices=[('N','Non-Veg'),('V',"Veg")])
    category=models.CharField(max_length=20,choices=[('B','Breakfast'),('L','Lunch'),('D','Dinner')])
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class RecipeHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    made_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} made {self.recipe.name} on {self.made_on}"
