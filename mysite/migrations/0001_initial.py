# Generated by Django 4.0.4 on 2022-05-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='leave start date is on ..', verbose_name='Start Date')),
                ('end_date', models.DateField(help_text='Leave Ends on', verbose_name='End Date')),
                ('leave_type', models.CharField(choices=[('sick', 'Sick'), ('casual', 'Casual Leave'), ('emergency', 'Emergency'), ('Maternity', 'Maternity')], max_length=20)),
                ('reason', models.CharField(help_text='Brief Reason for leave', max_length=300, verbose_name='Detailed Reason for Leave')),
                ('days_count', models.IntegerField()),
                ('status', models.BooleanField(default=0, max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
