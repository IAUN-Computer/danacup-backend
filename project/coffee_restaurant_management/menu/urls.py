#################################################
######### function based views and urls #########
#################################################

# from django.urls import path
# from .views import item_list, item_detail
#
# urlpatterns = [
#     path("item/list", item_list, name='item_listing'),
#     path("item/<int:pk>", item_detail, name='item_detail'),
#
# ]


from django.urls import path
from .views import (ItemListingAPIView, ItemDetailedAPIView,
                    CategoryListingAPIView, CategoryDetailedAPIView)

urlpatterns = [
    path("item/list", ItemListingAPIView.as_view(), name='item_listing'),
    path("item/<int:pk>", ItemDetailedAPIView.as_view(), name='item_detail'),
    path('cat/list', CategoryListingAPIView.as_view(), name='cat_listing'),
    path('cat/<int:pk>', CategoryDetailedAPIView.as_view(), name='cat-detail')
]
