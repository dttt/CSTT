# -*- coding: utf-8 -*-

from django.db import models
from tvdd.models import MacronutrientUserGroup


class MemberFuction(models.Model):
    name = models.CharField(u"Tên hàm", max_length=50)

    class Meta:
        abstract = True


class Parameter(models.Model):
    min = models.DecimalField(
        u"Điểm bằng 0", max_digits=6, decimal_places=2)
    max = models.DecimalField(
        u"Điểm bằng 1", max_digits=6, decimal_places=2)

    class Meta:
        abstract = True


class MFMG(MemberFuction):
    macronutrient_user_group = models.ForeignKey(MacronutrientUserGroup)

    def __unicode__(self):
        return u"%s %s" % (self.macronutrient_user_group, self.name)

    class Meta:
        verbose_name = u"Hàm phụ thuộc của chất dinh dưỡng"
        verbose_name_plural = u"Các hàm phụ thuộc của chất dinh dưỡng"


class MFEnergy(MemberFuction):

    def __unicode__(self):
        return u"Năng lượng %s" % self.name

    class Meta:
        verbose_name = u"Hàm phụ thuộc của năng lượng"
        verbose_name_plural = u"Các hàm phụ thuộc của năng lượng"


class MFStatus(MemberFuction):

    def __unicode__(self):
        return u"Thể trạng %s" % self.name

    class Meta:
        verbose_name = u"Hàm phụ thuộc của thể trạng"
        verbose_name_plural = u"Các hàm phụ thuộc của thể trạng"


class ParameterMG(Parameter):
    member_function = models.ForeignKey(MFMG)

    def __unicode__(self):
        return u"Parameter %s" % self.member_function


class ParameterEnergy(Parameter):
    member_function = models.ForeignKey(MFEnergy)

    def __unicode__(self):
        return u"Parameter %s" % self.member_function


class ParameterStatus(Parameter):
    member_function = models.ForeignKey(MFStatus)

    def __unicode__(self):
        return u"Parameter %s" % self.member_function
