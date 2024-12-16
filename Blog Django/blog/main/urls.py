from django.urls import path
from . import views

urlpatterns = [
# principal
    path('', views.IndexView.as_view(), name='index'),
    path('blogadd/', views.BlogView.as_view(), name='blog_form'),
]
