from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, ProductViewSet, CartViewSet, ProductResponse, ProductSingle

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('carts', CartViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/', ProductResponse.as_view()),
    path('products/<int:id>/', ProductSingle.as_view()),
    path('', include(router.urls)),
]
