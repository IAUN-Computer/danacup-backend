from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    """no docstring"""
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField(default=0)
    quantity = models.PositiveBigIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    materials = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.id} - {self.name}"



##############################################################
##################### how to use signals #####################
##############################################################

# from django.conf import settings
# from django.db.models.signals import post_save, pre_save, post_delete
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)


# @receiver(pre_save, sender=Item)
# def pre_save_item(sender, instance=None, created=False, **kwargs):
#     print('before save item')
#
#
# @receiver(post_save, sender=Item)
# def post_save_item(sender, instance=None, created=False, **kwargs):
#     print("after save item")
#
