from django.db import models


class UserGroup(models.Model):
    name = models.CharField("Ten cua nhom tuoi", max_length=50)
    begin_age = models.IntegerField("Tuoi bat dau")
    end_age = models.IntegerField("Tuoi ket thuc")

    def __unicode__(self):
        return self.name


class Macronutrient(models.Model):
    name = models.CharField("Ten cua chat dinh duong", max_length=30)
    equal_calories = models.IntegerField("Doi sang calories")

    def __unicode__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField("Ten loai mon an", max_length=30)

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField("Ten nguyen lieu", max_length=30)

    def __unicode__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField("Ten cua mon an", max_length=30)
    type = models.ForeignKey(DishType, verbose_name="Loai")
    vegan = models.BooleanField("Mon chay")
    calories = models.DecimalField(
        "Calories mon an cung cap", max_digits=6, decimal_places=2)
    protein = models.DecimalField("Chat dam", max_digits=6, decimal_places=2)
    fat = models.DecimalField("Chat beo", max_digits=6, decimal_places=2)
    carbohydrate = models.DecimalField(
        "Chat duong bot", max_digits=6, decimal_places=2)
    dietary_fiber = models.DecimalField(
        "Chat xo", max_digits=6, decimal_places=2)
    main_ingredient = models.ForeignKey(
        Ingredient, verbose_name="Nguyen lieu chinh")

    def __unicode__(self):
        return self.name
