# -*- coding: utf-8 -*-
from decimal import Decimal

from .helper import Function


class User(object):

    def __init__(self, data):
        weight = data['weight']
        height = data['height']
        age = data['age']
        sex = data['sex']
        activity_level = data['activity_level']
        function = Function()
        # Sự kiện loại 1
        self.weight = weight
        self.height = height
        self.sex = sex
        self.activity_level = activity_level
        self.age = age
        # Sự kiện loại 2
        self.user_group = function.get_user_group(self.age)
        self.status = function.get_status(
            function.get_bmi(height=Decimal(height), weight=Decimal(weight)))
        self.eer = function.get_eer(age=age, sex=sex, activity=activity_level)
        self.energy = function.get_energy(self)
        mu = function.get_macronutrient_value(self)
        self.protein = mu[0][1]
        self.fat = mu[1][1]
        self.carbohydrate = mu[2][1]
