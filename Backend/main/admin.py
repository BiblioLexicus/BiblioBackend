from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Comments)
admin.site.register(LibrariesData)
admin.site.register(LoanedWorks)
admin.site.register(UserList)
admin.site.register(WorkList)
