################################################
############ Function Based Views: #############
################################################

#from django.shortcuts import render
#from .models import Item
#from django.http import JsonResponse

# def item_list(request):
#     data_list = list()
#     items_obj = Item.objects.all()
#     for each_item in items_obj:
#         data = {
#             "name": each_item.name,
#             "price": each_item.price
#         }
#         data_list.append(data)
#     return JsonResponse({"data": data_list,
#                          "status_code": 200})
#
# def item_detail(request, pk):
#
#     try:
#         item_obj = Item.objects.get(id=pk)
#     except Item.DoesNotExist as exp:
#         return JsonResponse({"message": 'not found',
#                              "status_code": 404})
#     except Exception as exp:
#         return JsonResponse({"message": 'error',
#                              "status_code": 400})
#     data = {
#         "name": item_obj.name,
#         "price": item_obj.price,
#         "materials": item_obj.materials
#     }
#     return JsonResponse({"data": data, "status_code": 200})


################################################
#### Function Based Views with rest_framework ##
################################################

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Item
# from .serializer import ItemSer
#
#
# @api_view(['GET', "POST"])
# def item_list(request):
#     if request.method == "GET":
#         items_obj = Item.objects.all()
#         item_ser = ItemSer(items_obj, many=True)
#         return Response(data=item_ser.data)
#     if request.method == "POST":
#         data = request.data
#         item_ser = ItemSer(data=data)
#         if item_ser.is_valid():
#             #TODO: 1- save it, 2- send appropriate response
#             item_ser.save()
#             return Response(data=item_ser.data)
#         else:
#             #TODO: 1- raise appropriate error, 2- send response
#             errors = item_ser.errors
#             return Response(data=errors)
#
#
# @api_view(["GET", "DELETE", "PUT"])
# def item_detail(request, pk):
#     if request.method == "GET":
#         item_obj = Item.objects.get(id=pk)
#         item_ser = ItemSer(item_obj)
#         return Response(data=item_ser.data)
#     if request.method == "DELETE":
#         #TODO : 1- query: Database 2- delete 3- send appropriate response
#         item_obj = Item.objects.get(id=pk).delete()
#         return Response(data={"message": 'Item deleted!'})
#     if request.method == "PUT":
#         #TODO: 1- query: Database (2- update 3- save changes) -> serializer 4- send appropriate response
#         data = request.data
#         item_obj = Item.objects.get(id=pk)
#         item_ser = ItemSer(item_obj, data=data)
#         if item_ser.is_valid():
#             # TODO: 1- save 2- send response
#             item_ser.save()
#             return Response(data=item_ser.data)
#         else:
#             #TODO: 1- raise appropriate error 2- send response
#             errors = item_ser.errors
#             return Response(data=errors)


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Item, Category
from .serializer import ItemSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


class ItemListingAPIView(APIView):
    permission_classes = [IsAdminUser,]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        items_obj = Item.objects.all()
        item_ser = ItemSerializer(items_obj, many=True, context={'request': request})
        return Response(data=item_ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        item_ser = ItemSerializer(data=data)
        if item_ser.is_valid():
            item_ser.save()
            return Response(data=item_ser.data, status=status.HTTP_201_CREATED)
        else:
            errors = item_ser.errors
            return Response(data=errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class ItemDetailedAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, pk):
        item_obj = Item.objects.get(id=pk)
        item_ser = ItemSerializer(item_obj, context={'request': request})
        return Response(data=item_ser.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        item_obj = Item.objects.get(id=pk).delete()
        return Response(data={"message": 'Item deleted!'}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        data = request.data
        item_obj = Item.objects.get(id=pk)
        item_ser = ItemSerializer(item_obj, data=data)
        if item_ser.is_valid():
            item_ser.save()
            return Response(data=item_ser.data, status=status.HTTP_202_ACCEPTED)
        else:
            errors = item_ser.errors
            return Response(data=errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class CategoryListingAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        cate_obj = Category.objects.all()
        cate_ser = CategorySerializer(cate_obj, many=True, context={'request': request})
        return Response(data=cate_ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        cat_ser = CategorySerializer(data=data)
        if cat_ser.is_valid():
            cat_ser.save()
            return Response(data=cat_ser.data, status=status.HTTP_201_CREATED)
        else:
            errors = cat_ser.errors
            return Response(data=errors, status=status.HTTP_406_NOT_ACCEPTABLE)


class CategoryDetailedAPIView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request, pk):
        cat_obj = Category.objects.get(id=pk)
        cat_ser = CategorySerializer(cat_obj, context={'request': request})
        return Response(data=cat_ser.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        cat_obj = Category.objects.get(id=pk).delete()
        return Response(data={"message": 'Category deleted!'},
                        status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        data = request.data
        cat_obj = Category.objects.get(id=pk)
        cat_ser = CategorySerializer(cat_obj, data=data)
        if cat_ser.is_valid():
            cat_ser.save()
            return Response(data=cat_ser.data, status=status.HTTP_202_ACCEPTED)
        else:
            errors = cat_ser.errors
            return Response(data=errors, status=status.HTTP_406_NOT_ACCEPTABLE)
