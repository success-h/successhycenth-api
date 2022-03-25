from django.db import models


class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='images', null=True, blank=True)


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title