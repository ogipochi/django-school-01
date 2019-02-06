from django.urls import path
from blog import views

app_name='blog'

urlpatterns = [
    path('list/',views.article_list),
    path('detail/<int:id>/',views.article_detail),
]