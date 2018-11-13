from django.contrib import admin
from .models import ProfileImage, Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "bio", "profile_image"]
    list_filter = ["user"]
    search_fields = ["user__username"]

    class Meta:
        model = Profile


class ProfileImageAdmin(admin.ModelAdmin):
    list_display = ["id", "profile", "created"]

    class Meta:
        model = ProfileImage


admin.site.register(Profile, ProfileAdmin)

admin.site.register(ProfileImage, ProfileImageAdmin)

# Register your models here.
