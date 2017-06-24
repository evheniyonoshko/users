# -*- coding: utf-8 -*-

import csv
from io import StringIO

from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from customers.forms import UserAdminForm
from customers.models import User, Courses


class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    ordering = ('registered',)
    list_filter = ['is_active', ]

    list_display = (
        'email', 'first_name', 'last_name', 'name', 'phone', 'mobile_phone', 'is_superuser', 'is_active', 'is_staff',
    )

    fieldsets = (
        ('Info', {
            'fields': ('email', 'first_name', 'last_name', 'name', 'phone', 'mobile_phone')
        }),
        ('Permissions', {
            'fields': ('is_superuser','is_staff', 'is_active')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name',
                       'first_name', 'last_name', 'phone', 'mobile_phone')
        }),
        ('Permissions', {
            'fields': ('is_superuser', 'is_staff', 'is_active')
        }),
    )

    class Media:
        css = {
            # 'all': (
            #     'css/select2.min.css',
            #     'css/bootstrap.min.css',
            # )
        }
        js = (
            # 'js/jquery-3.1.0.min.js',
            # 'js/bootstrap.min.js',
            # 'js/select2.full.min.js',
            # 'js/select2.full.min.js',
            # 'js/js.cookie.js',
        )


class CoursesAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'code',)
    search_fields = ('name', )
    fields = ('name', 'code',)

admin.site.register(User, UserAdmin)
admin.site.register(Courses, CoursesAdmin)
