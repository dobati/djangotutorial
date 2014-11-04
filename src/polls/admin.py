from django.contrib import admin
from polls.models import UserInput
from polls.models import GeneralEnEs
from polls.models import SubsEnEs
from polls.models import EuconstEnEs
from polls.models import ThelittleprinceEnEs


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
