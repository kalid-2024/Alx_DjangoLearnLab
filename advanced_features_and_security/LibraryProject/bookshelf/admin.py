from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("title", "author", "publication_year")

    # Add filters on the right sidebar
    list_filter = ("author", "publication_year")

    # Add a search box
    search_fields = ("title", "author") 

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register your models here.
admin.site.register(Book, BookAdmin, CustomUser, CustomUserAdmin)