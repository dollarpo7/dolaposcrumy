from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'dolaposcrumy'

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('dolaposcrumy/adduser/', views.add_user, name='add_user'),
    # path('dolaposcrumy/addtask/', views.add_task, name='add_task'),
    path('dolaposcrumy/<int:pk>/edit_task/', views.edit_task, name='edit_task'),
    path('dolaposcrumy/accessdenied', views.user_passes_test, name = 'access_denied'),
    path('', views.GoalsListView.as_view(), name='home'),
    path('dolaposcrumy/new',views.GoalCreateView.as_view(), name='new_goal'),
    # path('dolaposcrumy/<int:pk>/edit/', views.GoalsUpdateView.as_view(), name='edit_goal'),
    path('dolaposcrumy/<int:pk>/delete/',views.DeleteGoalView.as_view(), name='delete_goal'),
]
