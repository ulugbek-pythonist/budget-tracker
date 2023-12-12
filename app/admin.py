from django.contrib import admin

from .models import Expense, Income, Profile, Wallet


admin.site.register(Profile)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Wallet)