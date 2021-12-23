from django.contrib.auth.models import User
from django.db                  import models
from django.db.models.fields    import IntegerField
from article.models             import Article



class Order(models.Model):
    user           = models.ForeignKey(User, related_name='orders',on_delete=models.CASCADE)
    name           = models.CharField(max_length=100)
    email          = models.CharField(max_length=100)
    address        = models.CharField(max_length=100)
    place          = models.CharField(max_length=100)
    date           = models.DateTimeField(auto_now_add=True)
    paid_amount    = models.IntegerField(default=0)
    stripe_token   = models.CharField(max_length=100)

    class Meta:
        ordering =['-date',]

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order    = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
    article  = models.ForeignKey(Article,related_name='items', on_delete=models.CASCADE)
    price    = models.IntegerField(default=0)
    quantity = IntegerField(default=1)

    
    def __str__(self):
        return '$s' % self.id


