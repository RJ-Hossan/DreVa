from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('add_dream/', views.add_dream, name='add_dream'),
    path('add_event/', views.add_event, name='add_event'),
]
