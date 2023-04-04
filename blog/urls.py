
from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.list_blog, name="list_blog"),
    path('detail/<int:id_article>', views.detail, name='detail')

]
