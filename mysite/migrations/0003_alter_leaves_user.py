# Generated by Django 4.0.4 on 2022-05-15 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_students_category'),
        ('mysite', '0002_leaves_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaves',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.students'),
        ),
    ]
