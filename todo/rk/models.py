from django.db import models

class Computer(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'computers'

class Program(models.Model):
    name = models.CharField(max_length=255)
    size = models.IntegerField()
    computer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'programs'