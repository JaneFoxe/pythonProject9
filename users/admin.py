from django.contrib import admin

from users.models import Payments, User

# Register your models here.
admin.site.register(Payments)
admin.site.register(User)