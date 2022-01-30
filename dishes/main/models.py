from django.db import models


TRANSPORT_CHOICES = [
('Courier delivery', 'Courier delivery'),
('Recipient pickup', 'Recipient pickup')
]


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250, null=True, blank=True)  
    note = models.TextField(blank=True)
    adv = models.CharField("תיאור לקידום", max_length = 500, null=True, blank=True)
    #transport = models.CharField(max_length=20, choices=TRANSPORT_CHOICES)
    def __str__(self):
        return str( self.first_name )


class Adv( models.Model ):
    main_adv = models.TextField("main_adv", max_length = 500, null=True, blank=True)
    catalog_adv = models.TextField("catalog_adv", max_length = 500, null=True, blank=True)
    about_adv = models.TextField("about_adv ", max_length = 500, null=True, blank=True)
    contact_adv = models.TextField("contact_adv ", max_length = 500, null=True, blank=True)

    def __str__(self):
        return str('adv')

