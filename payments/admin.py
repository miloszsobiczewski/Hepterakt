from django.contrib import admin
from .models import Payment, Category, Task, Month


admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Month)
