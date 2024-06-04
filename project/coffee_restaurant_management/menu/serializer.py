###################################################
############### simple serializers ################
###################################################

# from rest_framework import serializers
# from .models import Item


# def validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too shoooooooooooort :D')
#     if len(value) > 10:
#         raise serializers.ValidationError('Name is too bozorg :D')
#     return value

# class ItemSer(serializers.Serializer):
#     id = serializers.CharField(read_only=True)
#     name = serializers.CharField(max_length=100)
#     price = serializers.IntegerField()
#     quantity = serializers.IntegerField()
#     materials = serializers.JSONField()
#
#     """
#     how to add new item:
#     1- user input
#     2- validation
#     3- create item
#     """
#     def create(self, validated_data):
#         item = Item()
#         item.name = validated_data['name']
#         item.price = validated_data['price']
#         item.quantity = validated_data['quantity']
#         item.materials = validated_data['materials']
#         item.save()
#         return item
#
#     """
#     1- user input
#     2- instance
#     3- validation
#     4- update
#     """
#     def update(self, instance, validated_data):
#         # TODO for next session: how to handel fields that are not exists in request
#         # instance = Item.objects.get(id=pk)
#         instance.name = validated_data['name']
#         instance.price = validated_data['price']
#         instance.quantity = validated_data['quantity']
#         instance.materials = validated_data['materials']
#         instance.save()
#         return instance

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too shoooooooooooort :D')
    #     if len(value) > 10:
    #         raise serializers.ValidationError('Name is too bozorg :D')
    #     return value
    #
    #
    # def validate(self, data: dict):
    #     if data['price'] > 0 and data['quantity'] == 0:
    #         raise serializers.ValidationError('quantity should be positive')
    #     return data


# from rest_framework import serializers
# from .models import Item, Category
#
# class ItermSerializer(serializers.ModelSerializer):
#     # field_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Item
#         fields = "__all__"
#         # fields = ['id', 'name', 'price', "quantity", "field_name"]
#         # exclude = ['id']
#
#     # def get_field_name(self, obj):
#     #     return obj.price * obj.quantity
#
#
# class CategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Category
#         fields = '__all__'
#


from rest_framework import serializers
from .models import Item, Category

class ItemSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='name'
    # )
    # category = serializers.StringRelatedField()
    # category = serializers.PrimaryKeyRelatedField(read_only=True)
    # category = serializers.HyperlinkedRelatedField(
    #     read_only=True,
    #     view_name='cat-detail'
    # )

    class Meta:
        model = Item
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True,
                           read_only=True)

    # items = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )
    # items = serializers.StringRelatedField(many=True, read_only=True)
    # items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # items = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='item_detail'
    # )

    class Meta:
        model = Category
        fields = '__all__'
