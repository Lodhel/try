from django.db import models

class Test(models.Model):
    test = models.CharField(max_length=16)

    def __str__(self):
        return self.test