# Generated by Django 3.2.12 on 2022-03-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='contact/icons')),
            ],
        ),
    ]