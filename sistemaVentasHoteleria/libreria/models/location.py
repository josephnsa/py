from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.country.name}"


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.region.name}"
