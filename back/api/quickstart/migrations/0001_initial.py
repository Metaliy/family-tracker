# Generated by Django 5.0.4 on 2024-05-27 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('durations', models.DecimalField(decimal_places=1, max_digits=5)),
                ('place', models.CharField(max_length=100)),
            ],
        ),
    ]
