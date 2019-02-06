from django.urls import path
from blog import views

app_name='blog'

urlpatterns = [
    path('list/',views.article_list,name="list"),
    path('detail/<int:id>/',views.article_detail,name="detail"),
]