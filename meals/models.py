from django.db import models

class Items(models.Model):
    day_id = models.IntegerField()
    meal_id = models.IntegerField()
    item = models.CharField(max_length = 100)

    def __str__(self):
        return self.item
