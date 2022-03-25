from django.db import models


class Technology(models.Model):    
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons', null=True, blank=True, max_length=255)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name