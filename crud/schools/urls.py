
from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.SchoolList.as_view(), name='school_list'),
    path('<int:pk>/', views.SchoolDetail.as_view(), name='school_detail'),
    path('create/', views.SchoolCreate.as_view(), name='school_create'),
    path('update/<int:pk>/', views.SchoolUpdate.as_view(), name='school_update'),
    path('delete/<int:pk>/', views.SchoolDelete.as_view(), name='school_delete'),
]
