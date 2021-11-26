from django.db import models
from django.db.models.fields import CharField, FloatField

# Create your models here.

class TprLab1Strategy(models.Model):
    numStrategy = models.CharField(max_length=30, null=True)
    good_good = models.FloatField(null=True)
    good_bad = models.FloatField(null=True)
    bad_good = models.FloatField(null=True)
    bad_bad =  models.FloatField(null=True)
    
    def __str__(self):
            return str(self.numStrategy)


class TprLab1Dohod(models.Model):
    numDohod = models.CharField(max_length=30, null=True)
    good_good = models.FloatField(null=True)
    good_bad = models.FloatField(null=True)
    bad_good = models.FloatField(null=True)
    bad_bad =  models.FloatField(null=True)
    def __str__(self):
            return str(self.numDohod)


class TprLab1StrategyExample(models.Model):
    numStrategyExample = models.CharField(max_length=30, null=True)
    one_one = models.FloatField(null=True)
    one_two = models.FloatField(null=True)
    one_three = models.FloatField(null=True)
    two_one =  models.FloatField(null=True)
    two_two =  models.FloatField(null=True)
    two_three =  models.FloatField(null=True)
    three_one =  models.FloatField(null=True)
    three_two =  models.FloatField(null=True)
    three_three =  models.FloatField(null=True)
    
    def __str__(self):
            return str(self.numStrategyExample)


class TprLab1DohodsExample(models.Model):
    numDohodExample = models.CharField(max_length=30, null=True)
    one_one = models.FloatField(null=True)
    one_two = models.FloatField(null=True)
    one_three = models.FloatField(null=True)
    two_one =  models.FloatField(null=True)
    two_two =  models.FloatField(null=True)
    two_three =  models.FloatField(null=True)
    three_one =  models.FloatField(null=True)
    three_two =  models.FloatField(null=True)
    three_three =  models.FloatField(null=True)
    
    def __str__(self):
            return str(self.numDohodExample)