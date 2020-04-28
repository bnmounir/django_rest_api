from django.urls import path, include
from profile_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, base_name='hello_viewset')

urlpatterns = [
    path('apiview/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
