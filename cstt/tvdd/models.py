# -*- coding: utf-8 -*-

from django.db import models


class UserGroup(models.Model):
    name = models.CharField(u"Tên của nhóm tuổi", max_length=50)
    begin_age = models.IntegerField(u"Tuổi bắt đầu")
    end_age = models.IntegerField(u"Tuổi kết thúc")

    def __unicode__(self):
        return u'%s' % self.name


class Macronutrient(models.Model):
    name = models.CharField(u"Tên của chất dinh dưỡng", max_length=30)
    equal_calories = models.IntegerField(u"Đổi sang calories")

    def __unicode__(self):
        return u'%s' % self.name


class DishType(models.Model):
    name = models.CharField(u"Tên loại món ăn", max_length=30)

    def __unicode__(self):
        return u'%s' % self.name


class Ingredient(models.Model):
    name = models.CharField(u"Tên nguyên liệu", max_length=30)

    def __unicode__(self):
        return u'%s' % self.name


class Mealtime(models.Model):
    name = models.CharField("Tên bữa ăn", max_length=40)
    time = models.TimeField("Giờ thường ăn")

    def __unicode__(self):
        return u'%s' % self.name


class Dish(models.Model):
    name = models.CharField(u"Tên món ăn", max_length=30)
    type = models.ForeignKey(DishType, verbose_name=u"Loại")
    vegan = models.BooleanField(u"Là món chay?")
    calories = models.DecimalField(
        u"Calories cung cấp", max_digits=6, decimal_places=2)
    protein = models.DecimalField(
        u"Chất đạm cung cấp", max_digits=6, decimal_places=2)
    fat = models.DecimalField(
        u"Chất béo cung cấp", max_digits=6, decimal_places=2)
    carbohydrate = models.DecimalField(
        u"Chất đường bột cung cấp", max_digits=6, decimal_places=2)
    dietary_fiber = models.DecimalField(
        u"Chất xơ cung cấp", max_digits=6, decimal_places=2)
    main_ingredient = models.ForeignKey(
        Ingredient, verbose_name=u"Nguyên liệu chính")
    mealtime = models.ManyToManyField(Mealtime, null=True)

    def __unicode__(self):
        return u'%s' % self.name


class MacronutrientUserGroup(models.Model):
    macronutrient_id = models.ForeignKey(Macronutrient)
    user_group_id = models.ForeignKey(UserGroup)

    def __unicode__(self):
        return u"%s %s" % (self.macronutrient_id, self.user_group_id)


class Sex(models.Model):
    name = models.CharField(max_length=5)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u'Giới tính'
        verbose_name_plural = u'Các giới tính'


class ActivityLevel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        verbose_name = u'Mức độ hoạt động'
        verbose_name_plural = u'Các mức độ hoạt động'


class EER(models.Model):
    min_age = models.IntegerField(u'Tuổi bắt đầu')
    max_age = models.IntegerField(u'Tuổi kết thúc')
    sex = models.ForeignKey(Sex, verbose_name=u'Giới tính')
    calories = models.IntegerField()
    activity_level = models.ForeignKey(
        ActivityLevel, verbose_name=u'Mức độ hoạt động')
