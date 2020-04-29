from django.urls import path, include
from profile_app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, base_name='hello_viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('apiview/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view())
]
