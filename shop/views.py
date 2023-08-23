from .models import Product, UserProfile, Category
from rest_framework import generics
from rest_framework.viewsets import  ModelViewSet
from .serializers import ProductSerializer, UserProfileSerializer, CategorySerializer




class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer








