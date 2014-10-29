from django.contrib import admin
from polls.models import UserInput
from polls.models import TatoebaEnEs



class TranslationsAdmin(admin.ModelAdmin):
    fields = ['source', 'target']
    class Meta:
        model = TatoebaEnEs
admin.site.register(TatoebaEnEs, TranslationsAdmin)


class UserInputAdmin(admin.ModelAdmin):
    class Meta:
        model = UserInput
admin.site.register(UserInput, UserInputAdmin)
