from django.contrib import admin
from django.contrib.auth.models import Group, User

admin.site.site_header = 'World Glamour Tour Payment Administration'

admin.site.unregister(Group)
admin.site.unregister(User)
