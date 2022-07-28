from django.db import models
from django.contrib.auth.models import User



U_TYPE = (
    ('user','USER'),
    ('restaurant_owner', 'RESTAURANT_OWNER'),
)
# Create your models here.
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=U_TYPE, default='user')
    
    def __str__(self):
        return str(self.user.username)

class Shop(models.Model):
    owner = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='uid')
    name = models.CharField(max_length=100)

class Menu(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='shop')
    item_name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.shop.name)
