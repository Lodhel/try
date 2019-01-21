from django.db import models

class Test(models.Model):
    test = models.CharField(max_length=16)

    def __str__(self):
        return self.test


class AutoServices(models.Model):
    SERVICES_CHOICES = [('0', 'serOne'), ('1', 'serTwo')]
    services = models.CharField(max_length=1, choices=SERVICES_CHOICES)

    def __str__(self):
        return str(self.id)


class Vakans(models.Model):
    title = models.CharField(max_length=16)
    body = models.TextField()

    def __str__(self):
        return str(self.title)


class Resume(models.Model):
    title = models.CharField(max_length=16)
    body = models.TextField()

    def __str__(self):
        return str(self.title)


class Work(models.Model):
    vakans = models.ForeignKey(Vakans)
    resume = models.ForeignKey(Resume)

    def __str__(self):
        return str(self.id)

class Transport(models.Model):
    prokat = models.BooleanField(default=True)


class Auto(Transport):# аналогичны аодныц транспорт и т.д.
    pass#тут можнл мета дб и тау далее