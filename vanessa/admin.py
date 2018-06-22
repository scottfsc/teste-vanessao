from django.contrib import admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ('name', 'email', 'genero', 'idade')
    

