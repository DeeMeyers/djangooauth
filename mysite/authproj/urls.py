from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter
# router.register(r'get_delete_update_goal', views.get_delete_update_goal)
# router.register(r'get_post_goal', views.get_post_goal)

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.userpage, name='home'),
    path('home/pretty/', views.userpage2, name='althome'),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/goals/<int:pk>', views.get_delete_update_goal, name='get_delete_update_goal'),
    path('api/v1/goals/', views.get_post_goal, name='get_post_goal'),
    
]