# -*- coding: utf-8 -*-
from decimal import Decimal
import random

from tvdd.models import UserGroup, EER, MacronutrientUserGroup, Dish
from fuzzy.models import FuzzySet, FuzzyRule, Parameter, Domain


class MemberFunction(object):

    def get_value(self, value, parameter):
        min = parameter.min
        max = parameter.max
        value = Decimal(value)
        if (value >= min and value <= max) or (value <= min and value >= max):
            result = (value - min) / (max - min)
            return result


class Function(object):

    # Tìm nhóm người dùng
    def get_user_group(self, age):
        group = UserGroup.objects.filter(
            begin_age__lte=age,
            end_age__gte=age
        )
        return group

    # Tính BMI của một người
    def get_bmi(self, height, weight):
        return weight / (height * height)

    def get_bmr(self, height, weight, age, sex):
        s = 0
        if sex == 1:
            s = 5
        else:
            s = -161
        return ((10 * weight) + (6.25 * height) - (5 * age) + s)

    # Tìm các tập mờ thể trạng
    def get_status(self, bmi):
        helper = MemberFunction()
        status = []

        fuzzy_sets = FuzzySet.objects.filter(domain__id=1)
        for fuzzy_set in fuzzy_sets:
            for parameter in fuzzy_set.parameter_set.all():
                u = helper.get_value(bmi, parameter)
                if u is not None:
                    status.append((fuzzy_set, u))

        return status

    # Tìm trong db năng lượng tối thiểu cần thiết
    def get_eer(self, age, activity, sex):
        eer = EER.objects.get(
            min_age__lte=age,
            max_age__gte=age,
            activity_level=activity,
            sex=sex
        )
        return eer.calories

    # Hàm giải mờ
    def get_member_value(self, sets):
        m = 0
        total = 0
        for set in sets:
            m += set[1]
            total += Parameter.objects.filter(
                fuzzy_set=set[0])[0].max * set[1]

        return total / (m * 100)

    # Hàm tính năng lượng nạp vào hằng ngày
    def get_energy(self, user):
        sets = self.get_rule_result(status_sets=user.status, domain=2)
        return user.eer * (1 + self.get_member_value(sets))

    # Hàm tìm các miền giá trị của chất dinh dưỡng và độ tuổi
    def get_mu_domain(self, user_group):
        domains = []
        mu = MacronutrientUserGroup.objects.filter(user_group_id=user_group)
        for m in mu:
            domains.append(Domain.objects.get(special=m))

        return domains

    # Hàm tính lượng các chất dinh dưỡng cần
    def get_macronutrient_value(self, user):
        macronutrients = []
        result = []
        domains = self.get_mu_domain(user.user_group)
        for domain in domains:
            sets = self.get_rule_result(
                status_sets=user.status,
                domain=domain
            )
            macronutrients.append((
                domain.special.macronutrient_id, self.get_member_value(sets))
            )

        for m in macronutrients:
            result.append((m[0], (user.energy * m[1]) / m[0].equal_calories))

        return result

    # Hàm trả về vế sau của luật mờ
    def get_rule_result(self, status_sets, domain):
        energy_sets = []
        for status_set in status_sets:
            result = FuzzyRule.objects.get(
                supposition=status_set[0],
                result__domain=domain
            ).result
            energy_sets.append((result, status_set[1]))

        return energy_sets


class StaticValue(object):
    SAI_SO_L = Decimal(1.2)
    SAI_SO_N = Decimal(0.8)
    MAX_BOWLS = Decimal(4)
    RICE = Dish.objects.get(pk=1)

    @staticmethod
    def get_rice_calories():
        return StaticValue.MAX_BOWLS * StaticValue.RICE.calories

    @staticmethod
    def get_rice_protein():
        return StaticValue.MAX_BOWLS * StaticValue.RICE.protein

    @staticmethod
    def get_rice_fat():
        return StaticValue.MAX_BOWLS * StaticValue.RICE.fat

    @staticmethod
    def get_rice_carbohydrate():
        return StaticValue.MAX_BOWLS * StaticValue.RICE.carbohydrate


class DishFunction(object):

    def get_random(self):
        breakfast_type = [2, 3, 4, 13, 14, 15, 16, 17, 20]
        #exclude_breakfast = [1, 6, 12, 28, 19, 21, 22]
        breakfast = {
            'canh': random.choice(
                Dish.objects.filter(type__in=breakfast_type).exclude(id=1)
            ),
            'man': None
        }
        #exclude_list = [3, 6, 4, 14, 15, 16, 17, 20, 4, 18, 29, 21]
        rice_list = [1, 5, 8, 9, 10, 11, 21]
        #dinner = random.choice(Dish.objects.exclude(type__in=exclude_list))
        #lunch = random.choice(Dish.objects.exclude(type__in=exclude_list))
        lunch = {
            'canh': self.get_canh(),
            'man': self.get_man()
        }

        dinner = {
            'canh': self.get_canh(),
            'man': self.get_man()
        }
        return [breakfast, lunch, dinner]

    # Tìm ra một canh
    def get_canh(self, exclude_list=None):
        if exclude_list is not None:
            canh = random.choice(
                Dish.objects.filter(type=1).exclude(id__in=exclude_list)
            )
        else:
            canh = random.choice(
                Dish.objects.filter(type=1)
            )
        return canh

    # Tìm ra món mặn
    def get_man(self, exclude_list=None):
        man_list = [5, 9, 8, 10, 11]
        if exclude_list is not None:
            man = random.choice(
                Dish.objects.filter(type__in=man_list).exclude(id__in=exclude_list)
            )
        else:
            man = random.choice(Dish.objects.filter(type__in=man_list))

        return man

    def get_total_calories(self, dishes):
        total = 0
        for dish in dishes:
            canh = dish.get('canh', None)
            man = dish.get('man', None)
            if canh is not None and man is not None:
                total += (canh.calories + man.calories)
            elif canh is not None:
                total += canh.calories
            elif man is not None:
                total += man.calories

        return total

    def get_total_protein(self, dishes):
        total = 0
        for dish in dishes:
            canh = dish.get('canh', None)
            man = dish.get('man', None)
            if canh is not None and man is not None:
                total += (canh.protein + man.protein)
            elif canh is not None:
                total += canh.protein
            elif man is not None:
                total += man.protein

        return total

    def get_total_fat(self, dishes):
        total = 0
        for dish in dishes:
            canh = dish.get('canh', None)
            man = dish.get('man', None)
            if canh is not None and man is not None:
                total += (canh.fat + man.fat)
            elif canh is not None:
                total += canh.fat
            elif man is not None:
                total += man.fat

        return total

    def get_total_carbohydrate(self, dishes):
        total = 0
        for dish in dishes:
            canh = dish.get('canh', None)
            man = dish.get('man', None)
            if canh is not None and man is not None:
                total += (canh.carbohydrate + man.carbohydrate)
            elif canh is not None:
                total += canh.carbohydrate
            elif man is not None:
                total += man.carbohydrate

        return total

    def check(self, user, dishes):
        result_protein = False
        result_fat = False
        result_carbohydrate = False
        result_calories = False

        dishes_protein = self.get_total_protein(dishes=dishes)
        dishes_protein += StaticValue.get_rice_protein()

        dishes_fat = self.get_total_fat(dishes=dishes)
        dishes_fat += StaticValue.get_rice_fat()

        dishes_carbohydrate = self.get_total_carbohydrate(dishes=dishes)
        dishes_carbohydrate += StaticValue.get_rice_carbohydrate()

        dishes_calories = self.get_total_calories(dishes=dishes)
        dishes_calories += StaticValue.get_rice_calories()

        l = StaticValue.SAI_SO_L
        n = StaticValue.SAI_SO_N

        protein_l = user.protein * l
        protein_n = user.protein * n

        fat_l = user.fat * l
        fat_n = user.fat * n

        carbohydrate_l = user.carbohydrate * l
        carbohydrate_n = user.carbohydrate * n

        calories_l = user.energy * l
        calories_n = user.energy * n

        if dishes_calories <= calories_l and dishes_calories >= calories_n:
            result_calories = True

        if dishes_protein <= protein_l and dishes_protein >= protein_n:
            result_protein = True

        if dishes_fat <= fat_l and dishes_fat >= fat_n:
            result_fat = True

        if dishes_carbohydrate <= carbohydrate_l and dishes_carbohydrate >= carbohydrate_n:
            result_carbohydrate = True

        if result_calories: #and result_carbohydrate and result_fat and result_protein:
            return True
        else:
            return False

    def get_menu(self, user):
        dishes = self.get_random()
        while self.check(dishes=dishes, user=user) is False:
            dishes = self.get_random()

        return dishes
