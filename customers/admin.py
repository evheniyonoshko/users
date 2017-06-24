# -*- coding: utf-8 -*-

import csv
from io import StringIO

from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from customers.forms import UserAdminForm
from customers.models import User, Courses, Customers


class UserAdmin(BaseUserAdmin):
    form = UserAdminForm
    ordering = ('registered',)
    list_filter = ['is_active', ]

    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_active', 'is_staff',
    )

    fieldsets = (
        ('Info', {
            'fields': ('username', 'email', 'first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('is_superuser','is_staff', 'is_active')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username',
                       'first_name', 'last_name')
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


class CustomersAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ('name', 'email', 'phone', 'mobile_phone', 'status')
    search_fields = ('name',)
    fields = ('name', 'email', 'phone', 'mobile_phone', 'status')


admin.site.register(User, UserAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Customers, CustomersAdmin)
