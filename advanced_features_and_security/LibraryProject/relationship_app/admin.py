from django.contrib import admin
from .models import Book, Author, Librarian, Library, CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    fieldsets = UserAdmin.fieldsets +(
        (_("Custom Fields"),{
            "fields":("date_of_birth", "phone_number", "is_verified")
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Custom Fields"),{
            "fields":("date_of_birth", "phone_number", "is_verified")
        }),
    )
    list_display = (
        "username", "email", "first_name", "last_name",
        "is_staff", "is_verified", "phone_number"
    )
    list_filter = ("is_staff", "is_superuser", "is_verified", "is_active")
    

admin.site.register(CustomUser, CustomUserAdmin)