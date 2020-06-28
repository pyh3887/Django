
# Register your models here.
from django.contrib import admin
from myfriend.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','irum','nai','juso')

admin.site.register(Article, ArticleAdmin) #관리자 테이블에 추가하고싶을경우
