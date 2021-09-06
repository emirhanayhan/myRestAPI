from django.db import models


class users(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    mail = models.CharField(max_length=60)
    status = models.IntegerField()


class users_trip(models.Model):
    tripId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(users, on_delete=models.CASCADE)
    totalDistance = models.IntegerField()
    beginningTime = models.CharField(max_length=10)
