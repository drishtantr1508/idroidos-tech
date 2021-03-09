from django.contrib import admin
from .models import (UserProfileInfo,ComparisonInfo,SmartphonesInfo,NewsArticle
                    ,SmartphoneComment,NewsComment,ComparisonComment,QuickLinks)
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(ComparisonInfo)
admin.site.register(SmartphonesInfo)
admin.site.register(NewsArticle)
admin.site.register(SmartphoneComment)
admin.site.register(ComparisonComment)
admin.site.register(NewsComment)
admin.site.register(QuickLinks)
