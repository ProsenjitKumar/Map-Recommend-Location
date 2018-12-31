from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'birth_date', 'friends', 'following', 'follower']
    list_filter = ['user', 'bio', 'birth_date', 'friends', 'following', 'follower']
    search_fields = ['user', 'bio', 'birth_date', 'friends', 'following', 'follower']
    list_editable = ['bio', 'birth_date', 'friends', 'following', 'follower']
    list_per_page = 25


admin.site.register(UserAccount, UserAccountAdmin)
