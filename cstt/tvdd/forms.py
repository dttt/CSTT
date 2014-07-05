# -*- coding: utf-8 -*-
import floppyforms as forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from crispy_forms.bootstrap import InlineRadios

from tvdd.models import Sex, ActivityLevel

class UserForm(forms.Form):
    age = forms.IntegerField(
        label="Tuổi",
        required=True
    )
    sex = forms.ModelChoiceField(
        queryset=Sex.objects.all(),
        label=u'Giới tính',
        empty_label=None
    )
    height = forms.DecimalField(
        label="Chiều cao",
        required=True,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Đơn vị là cm'}
        )
    )
    weight = forms.DecimalField(
        label="Cân nặng",
        required=True,
        widget=forms.NumberInput(
            attrs={'placeholder': 'Đơn vị là kg'}
        )
    )
    activity_level = forms.ModelChoiceField(
        queryset=ActivityLevel.objects.all(),
        label=u'Mức độ hoạt động',
        empty_label=None,
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_class = "form-horizontal"
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.html5_required = True
        self.helper.layout = Layout(
            'age',
            'height',
            'weight',
            InlineRadios('sex'),
            'activity_level',
        )
        self.helper.add_input(Submit('submit', 'Tư vấn'))
