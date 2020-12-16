from django.db import models


# Create your models here.
class Osoba(models.Model):
    imie = models.CharField(max_length=60, null=True)
    nazwisko = models.CharField(max_length=60, null=False)
    data_urodzenia = models.DateField(null=True)
    email = models.CharField(max_length=100, unique=True, null=True)
    zarobki = models.DecimalField(max_digits=10, decimal_places=2, default=4000, null=True)

    def __str__(self):
        return str(self.imie) + ' ' + str(self.nazwisko) + ' ' + str(self.data_urodzenia)


class Samochod(models.Model):
    marka = models.CharField(max_length=60, null=False, default="Fiat")
    model = models.CharField(max_length=60, null=False)
    pojemnosc = models.IntegerField()
    rok_produkcji = models.DateField()
    wlasciciel = models.ForeignKey(Osoba, related_name='samochody', on_delete=models.SET_NULL, null=True)
    wlasciciel_uzytkownik = models.ForeignKey('auth.User', related_name='samochody', on_delete=models.CASCADE)

















