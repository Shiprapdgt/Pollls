from django.contrib import admin


# Register your models here.
from UserProfile.models import Token

admin.site.register(Token)