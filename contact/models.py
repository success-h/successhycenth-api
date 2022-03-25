from django.db import models


class Contact(models.Model):
    link = models.CharField(max_length=250, blank=True, null=True)
    icon = models.ImageField(upload_to='contact/icons', blank=True, null=True)
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    