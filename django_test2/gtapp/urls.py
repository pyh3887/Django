

from django.urls import path
from gtapp import views


urlpatterns = [
    path('insert', views.InsertFunc, name = 'InsertFunc'), # Including another URLcon
    path('insertok', views.InsertokFunc, name = 'InsertokFunc'),
]


 
