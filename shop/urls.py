from django.urls import path, include
from .views import UserProfileDetailView, ProductViewSet, CategoryViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ProductViewSet)
router.register('category', CategoryViewSet)


urlpatterns = [
    path('viewset/', include(router.urls)),

    path('profile/<int:pk>/', UserProfileDetailView.as_view(), name='user-profile'),
    
] 
