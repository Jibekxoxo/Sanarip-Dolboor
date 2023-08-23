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



# def search_result(request):
#     item = request.GET.get('item')
#     print(item)
#     products = Product.objects.filter(name__icontains=item) #ищу по логике in, то есть все, что содержит
#     context ={
#         'products': products, 
#     }
#     return render(request, 'search_result.html', context=context)




