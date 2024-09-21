from django.db import models


class Owner(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Achievement(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    

class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        Owner, related_name='cats', on_delete=models.CASCADE)
    achievements = models.ManyToManyField(Achievement,
                                          related_name='cats', blank=True)


    def __str__(self):
        return self.name
    
