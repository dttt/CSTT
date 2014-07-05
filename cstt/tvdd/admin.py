from django.contrib import admin


from .models import (
    Dish, DishType, Ingredient, Macronutrient,
    UserGroup, MacronutrientUserGroup, Sex, ActivityLevel,
    EER, Mealtime)


admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(Ingredient)
admin.site.register(Macronutrient)
admin.site.register(MacronutrientUserGroup)
admin.site.register(UserGroup)
admin.site.register(EER)
admin.site.register(Sex)
admin.site.register(ActivityLevel)
admin.site.register(Mealtime)
