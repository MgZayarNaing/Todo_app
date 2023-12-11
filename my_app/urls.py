from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from my_app.views import  task_views

urlpatterns = [


    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('task/all', task_views.TaskIndex),
    path('task/add', task_views.TaskStore),
    path('task/view/<int:pk>', task_views.TaskShow),
    path('task/change/<int:pk>', task_views.TaskUpdate),
    path('task/delete/<int:pk>', task_views.TaskDelete),

]