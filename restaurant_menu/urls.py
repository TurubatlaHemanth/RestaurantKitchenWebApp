from django.urls import path
from . import views

urlpatterns=[
    path('',views.MenuList.as_view(), name='homepage'),
    path('item/<int:pk>',views.MenuItemDetail.as_view(), name='menu_itemdetail')
]