# Generated by Django 4.0.4 on 2022-05-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='category',
            field=models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], default='S', max_length=1),
        ),
    ]
