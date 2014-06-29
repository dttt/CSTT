from decimal import Decimal

from tvdd.models import UserGroup, EER
from fuzzy.models import FuzzySet


class MemberFunction(object):

    def get_function(self):
        pass

    def get_value(self, value, parameter):
        min = parameter.min
        max = parameter.max
        value = Decimal(value)
        if (value >= min and value <= max) or (value <= min and value >= max):
            result = (value - min) / (max - min)
            return result


class Function(object):

    def get_user_group(self, age):
        groups = UserGroup.objects.all()
        for group in groups:
            if age >= group.begin_age and age <= group.end_age:
                return group

    def get_bmi(self, height, weight):
        return weight / (height * height)

    def get_bmr(self, height, weight, age, sex):
        s = 0
        if sex == 1:
            s = 5
        else:
            s = -161
        return ((10 * weight) + (6.25 * height) - (5 * age) + s)

    def get_status(self, bmi):
        helper = MemberFunction()
        status = []

        fuzzy_sets = FuzzySet.objects.filter(domain_id=1)
        for fuzzy_set in fuzzy_sets:
            for parameter in fuzzy_set.parameter_set.all():
                u = helper.get_value(bmi, parameter)
                if u is not None:
                    status.append((fuzzy_set, u))

        return status

    def get_eer(self, age, activity, sex):
        eer = EER.objects.filter(
            min_age__gte=age,
            max_age__lte=age,
            activity_level=activity,
            sex=sex
        )[0]
        return eer.calories
