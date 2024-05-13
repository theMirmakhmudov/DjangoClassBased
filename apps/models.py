from django.db import models


class People(models.Model):
    fullname = models.CharField(max_length=255)
    jobs = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', null=True, blank=True, default="default-user.png")

    def __str__(self):
        return self.fullname
