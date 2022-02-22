# Generated by Django 3.2.7 on 2022-02-22 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_animal_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='types',
            field=models.CharField(blank=True, choices=[('h', 'Хищник'), ('t', 'Травоядный')], max_length=50, null=True),
        ),
    ]
