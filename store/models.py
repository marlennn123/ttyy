from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)


    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name


class Comment(models.Model):
    user = models.CharField(max_length=16)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user} - {self.product}'