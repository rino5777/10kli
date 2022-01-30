from django.db import models
from catalog.models import Product




ORDER_STATUS = [
('Created', 'Created'),
('Processing', 'Processing'),
('Shipped', 'Shipped'),
('Ready for pickup', 'Ready for pickup'),
('Completed', 'Completed')
]
TRANSPORT_CHOICES = [
('Courier delivery', 'Courier delivery'),
('Recipient pickup', 'Recipient pickup')
]


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    
    city = models.CharField(max_length=100)
    
    
    note = models.TextField(blank=True)
    
    

    class Meta:
      
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


    def __str__(self):
        return f'Order #{self.id}'


   


class OrderItem(models.Model):
    order = models.ForeignKey( Order, related_name='items', on_delete=models.CASCADE )
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return str(self.id)

    