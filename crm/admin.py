from django.contrib import admin

from crm.models import Order, Status, Comment

admin.site.register(Order)
admin.site.register(Status)
admin.site.register(Comment)
