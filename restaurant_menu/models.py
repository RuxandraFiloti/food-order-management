from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
    ("beverages", "Beverages"),
)

STATUS = (
    ("0", "Available"),
    ("1", "Unavailable"),
    
)
# Create your models here.
class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True) # Unique meal name
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)  # CASCADE means if the user is deleted, their items are also deleted, 
                                                               #PROTECT doesnt delete the user and the item is not deleted,
                                                               #SET_NULL sets the author to null if the user is deleted
    status = models.IntegerField(choices=STATUS, default=0)  
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set the date when the item is created
    date_updated = models.DateTimeField(auto_now=True)  # Automatically set the date when the item is updated

    def __str__(self):
        return self.meal
    
  
