from email.policy import default
from django.db import models


class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    icon = models.FileField(upload_to='about/', null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title