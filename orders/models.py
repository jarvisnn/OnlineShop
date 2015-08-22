from django.db import models

# Create your models here.

class Order(models.Model):
    customer = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=200)
    address = models.TextField()
    note = models.TextField()
    products = models.TextField()
    price = models.FloatField(default=0)
    status = models.CharField(max_length=200)

    def __str__(self):
        return '[status: '+ str(self.status) + '] ' +\
            'id:' + str(self.id) +\
            '___name:' + str(self.customer) +\
            '___products:' + str(self.products) +\
            '___note:' + str(self.note) +\
            '___phone:' + str(self.phoneNumber) +\
            '___address:' + str(self.address);
