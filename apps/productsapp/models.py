from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ProductManager(models.Manager):
    def create_product(self, data):

        create = Product.objects.create(
        name = data['name'],
        description = data['description'],
        price = data['price'],
        )
        print create, "<---"
        return (True, create)

    def edit_product(self, data):
        edit= Product.objects.get(id = data['id'])
        edit.name,edit.description,edit.price = (data['name'],data['description'], data['price'])
        edit.save()
        return (edit)
        # edit.name.add(data['name'])
        # edit.description=data['description']
        # edit.price=data['price']
        # edit.save()


        # edit[0].name = data['name']
        # edit[0].description = data['description']
        # edit[0].price = data['price']
        # edit[0].save()




class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()

    def __unicode__(self):
        return unicode(self.id)+" "+ self.name+" "+self.description+" "+unicode(self.price)
