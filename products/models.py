from django.db import models
import os

# Create your models here.


class CategoryLevel2(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    upperCategory = models.ForeignKey(CategoryLevel2)

    def __str__(self):
        return "[" + self.upperCategory.name + "] " + self.name


def get_image_path(instance, filename):
    return 'product-images/' + filename


class Product(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(default=0)
    view = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to=get_image_path, null=True)

    def __str__(self):
        return "[ID: " + str(self.id) + "] " + self.name


class Image(models.Model):
    product = models.ForeignKey(Product, null=True)
    image = models.ImageField(upload_to=get_image_path, null=True)

    def __str__(self):
        return "[productID: " + str(self.product.id) + ", imgID: " + str(self.id) + "] " + str(self.image)


class SlideImage(models.Model):
    image = models.ImageField(upload_to=get_image_path, null=True)

    def __str__(self):
        return str(self.image)
