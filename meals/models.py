from django.db import models

class Members(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length=25)
    netid = models.CharField(max_length=25)
    staff = models.BooleanField()

    def __str__(self):
        return self.netid

class Items(models.Model):
    day_id = models.IntegerField()
    meal_id = models.IntegerField()
    item = models.CharField(max_length = 800)

    def __str__(self):
        return self.item
