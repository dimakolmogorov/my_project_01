from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self):
        return f"User: {self.name}, \nEmail: {self.email}, \nAge: {self.age}"


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')


class Order(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)


class Author(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'
