from django.contrib import admin


from .models import Dish, DishType, Ingredient, Macronutrient


admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(Ingredient)
admin.site.register(Macronutrient)
