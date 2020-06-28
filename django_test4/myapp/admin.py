from django.contrib import admin
from myapp.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','code','sang','price','pub_date')

admin.site.register(Article, ArticleAdmin) #관리자 테이블에 추가하고싶을경우
