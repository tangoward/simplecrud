# Generated by Django 2.0.1 on 2018-01-02 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('principal', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=150)),
                ('number_of_students', models.PositiveIntegerField()),
            ],
        ),
    ]
