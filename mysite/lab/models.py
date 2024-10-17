from datetime import timezone, datetime, date

from django.db import models


# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')
GENDER = models.IntegerChoices('Płeć', 'Kobieta Mężczyzna Inne')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2, default='PL')

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateField("Date Published")
    workers = models.IntegerField(default=0)

#Zadamie 1
#Model Stanowisko
class Stanowisko(models.Model):
    nazwa = models.CharField(null=False, blank=False, max_length=20)
    opis = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.nazwa}"

#Model Osoba
class Osoba(models.Model):
    imie = models.CharField(null=False, blank=False, max_length=20)
    nazwisko = models.CharField(null=False, blank=False, max_length=20)
    plec = models.IntegerField(choices=GENDER.choices)
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.imie + " " + self.nazwisko}"

    class Meta:
        ordering = ["nazwisko"]

