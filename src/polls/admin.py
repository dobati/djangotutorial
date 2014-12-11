from django.contrib import admin
from .models import UserInput
from .models import GeneralEnEs
from .models import SubsEnEs
from .models import EuconstEnEs
from .models import ThelittleprinceEnEs


class TranslationsAdminG(admin.ModelAdmin):
    fields = ['source', 'target']
    class Meta:
        model = GeneralEnEs
admin.site.register(GeneralEnEs, TranslationsAdminG)


class TranslationsAdminM(admin.ModelAdmin):
    fields = ['source', 'target']
    class Meta:
        model = SubsEnEs
admin.site.register(SubsEnEs, TranslationsAdminM)


class TranslationsAdminL(admin.ModelAdmin):
    fields = ['source', 'target']
    class Meta:
        model = EuconstEnEs
admin.site.register(EuconstEnEs, TranslationsAdminL)


class TranslationsAdminB(admin.ModelAdmin):
    fields = ['source', 'target']
    class Meta:
        model = ThelittleprinceEnEs
admin.site.register(ThelittleprinceEnEs, TranslationsAdminB)


class UserInputAdmin(admin.ModelAdmin):
    class Meta:
        model = UserInput
admin.site.register(UserInput, UserInputAdmin)
