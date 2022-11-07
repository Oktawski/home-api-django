from django.db import models

class Category(models.Model):
    CATEGORIES = (
        ('vegetables', 'Vegetables'),
        ('fruit', 'Fruit')
    )
    name = models.CharField(primary_key=True, max_length=20, choices=CATEGORIES)

    class Meta:
        db_table = "Categories"

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField(null=False, default=0)
    
