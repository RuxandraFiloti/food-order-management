from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),  # URL for the menu list page 
    path('item/<int:pk>/', views.MenuDetail.as_view(), name="menu_item") #int:pk -> dynamic urls
]

