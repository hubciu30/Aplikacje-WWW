from django.db import models

class Client(models.Model):
    firstname = models.CharField(max_length=60, null=True)
    surname = models.CharField(max_length=60, null=False)
    birthday = models.DateField(null=True)
    mail = models.CharField(max_length=100, unique=True, null=True)

    def __str__(self):
        return str(self.firstname) + ' ' + str(self.surname) + ' ' + str(self.birthday)


class Video(models.Model):
    title = models.CharField(max_length=60, null=True)
    year = models.IntegerField()
    director = models.CharField(max_length=60, null=True)
    type = models.CharField(max_length=60, null=True)
    owner = models.ForeignKey(Client, related_name='videos', on_delete=models.SET_NULL, null=True)
