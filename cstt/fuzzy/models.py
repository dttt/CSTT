# -*- coding: utf-8 -*-
from django.db import models
from tvdd.models import MacronutrientUserGroup


class Domain(models.Model):
    name = models.CharField("Tên miền", max_length=50)
    special = models.ForeignKey(MacronutrientUserGroup, blank=True, null=True)

    def __unicode__(self):
        return self.name


class FuzzySet(models.Model):
    name = models.CharField("Tên tập mờ", max_length=50)
    domain = models.ForeignKey(Domain, verbose_name="Miền xác định")

    def __unicode__(self):
        return u'%s - %s' % (self.domain, self.name)

    class Meta:
        verbose_name = "Tập mờ"
        verbose_name_plural = "Các tập mờ"


class Parameter(models.Model):
    fuzzy_set = models.ForeignKey(FuzzySet, verbose_name="Hàm của tập")
    min = models.DecimalField("Giá trị bằng 0", max_digits=5, decimal_places=2)
    max = models.DecimalField("Giá trị bằng 1", max_digits=5, decimal_places=2)

    def __unicode__(self):
        return u'Tham số cho %s' % self.fuzzy_set


class FuzzyRule(models.Model):
    supposition = models.ForeignKey(FuzzySet, related_name="supposition")
    activity_level = models.IntegerField(
        "Mức độ hoạt động", blank=True, null=True)
    result = models.ForeignKey(FuzzySet, related_name="result")

    def __unicode__(self):
        if self.activity_level:
            return u'If %s and mức độ hoạt động = %s then %s' % (
                self.supposition, self.activity_level, self.result)
        else:
            return u'If %s then %s' % (self.supposition, self.result)

    class Meta:
        verbose_name = "Luật mờ"
        verbose_name_plural = "Các luật mờ"
