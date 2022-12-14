from django.contrib import admin
from .models import Member

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_no', 'email', 'join_date']

    class Meta:
        model = Member

admin.site.register(Member, MemberAdmin)