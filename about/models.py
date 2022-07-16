from email.policy import default
from django.db import models
from .validators import validate_file_extension


class About(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='about/', null=True, blank=True, default=None, validators=[validate_file_extension])

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title