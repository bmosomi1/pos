from django.db import models
from django.forms import model_to_dict


class Category(models.Model):
    STATUS_CHOICES = (  # new
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive")
    )

    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=100,
        verbose_name="Status of the category",
    )

    class Meta:
        # Table's name
        db_table = "Category"
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    STATUS_CHOICES = (  # new
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive")
    )

    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=100,
        verbose_name="Status of the order",
    )

    class Meta:
        # Table's name
        db_table = "order"
        verbose_name_plural = "orders"

    def __str__(self) -> str:
        return self.name




class Product(models.Model):
    STATUS_CHOICES = (  # new
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive")
    )

    name = models.CharField(max_length=256)
    description = models.TextField(max_length=256)
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=100,
        verbose_name="Status of the product",
    )
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE, db_column='category')

    price = models.FloatField(default=0)

    class Meta:
        # Table's name
        db_table = "Product"

    def __str__(self) -> str:
        return self.name

    def to_json(self):
        item = model_to_dict(self)
        item['id'] = self.id
        item['text'] = self.name
        item['category'] = self.category.name
        item['quantity'] = 1
        item['total_product'] = 0
        return item



class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, models.DO_NOTHING, db_column='sale')
    product = models.ForeignKey(
        Product, models.DO_NOTHING, db_column='product')
    price = models.FloatField()
    quantity = models.IntegerField()
    total_detail = models.FloatField()

    class Meta:
        db_table = 'OrderDetails'

    def __str__(self) -> str:
        return "Detail ID: " + str(self.id) + " Order ID: " + str(self.order.id) + " Quantity: " + str(self.quantity)
