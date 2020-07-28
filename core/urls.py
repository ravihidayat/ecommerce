from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from .views import *

schema_view = get_swagger_view(title='BOOKSTORE API')

urlpatterns = [
    
    path('api-docs/', schema_view),

    path('', ApiRoot.as_view(), name=ApiRoot.name),

    path('address', AddressListView.as_view(), name=AddressListView.name),
    path('address/<str:pk>', AddressDetail.as_view(), name=AddressDetail.name),

    path('clients', ClientListView.as_view(), name=ClientListView.name),
    path('clients/<str:pk>', ClientDetail.as_view(), name=ClientDetail.name),

    path('status', StatusListView.as_view(), name=StatusListView.name),
    path('status/<str:pk>', StatusDetail.as_view(), name=StatusDetail.name),

    path('categories', CategoryListView.as_view(), name=CategoryListView.name),
    path('categories/<str:pk>', CategoryDetail.as_view(), name=CategoryDetail.name),
    
    path('authors', AuthorListView.as_view(), name=AuthorListView.name),
    path('authors/<str:pk>', AuthorDetail.as_view(), name=AuthorDetail.name),

    path('writes', WriteListView.as_view(), name=WriteListView.name),
    path('writes/<str:pk>', WriteDetail.as_view(), name=WriteDetail.name),

    path('books', BookListView.as_view(), name=BookListView.name),
    path('books/<str:pk>', BookDetail.as_view(), name=BookDetail.name),

    path('orders', OrderListView.as_view(), name=OrderListView.name),
    path('orders/<str:pk>', OrderDetail.as_view(), name=OrderDetail.name),

    path('itemsorders', ItemOrderListView.as_view(), name=ItemOrderListView.name),
    path('itemsorders/<str:pk>', ItemOrderDetail.as_view(), name=ItemOrderDetail.name),

    path('creditscards', CreditCardListView.as_view(), name=CreditCardListView.name),
    path('creditscards/<str:pk>', CreditCardDetail.as_view(), name=CreditCardDetail.name),

    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]

