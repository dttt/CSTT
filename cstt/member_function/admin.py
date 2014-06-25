from django.contrib import admin

from .models import (
    MFEnergy, MFMG, MFStatus,
    ParameterEnergy, ParameterMG, ParameterStatus)


admin.site.register(MFEnergy)
admin.site.register(MFMG)
admin.site.register(MFStatus)
admin.site.register(ParameterEnergy)
admin.site.register(ParameterMG)
admin.site.register(ParameterStatus)
