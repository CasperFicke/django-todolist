from django.db import models

# Create your models here.
class Item(models.Model):
  item_name = models.CharField(max_length=200)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.item_name + ' | ' + str(self.completed)
