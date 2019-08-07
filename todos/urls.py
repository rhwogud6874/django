from django.urls import path
from . import views

urlpatterns = [
    # 밑에 있는 코드는 create 하기 위한 코드
    path('new/', views.new),
    path('create/', views.create),
    # Read
    path('', views.index),
    path('<int:todo_id>/', views.detail),
]