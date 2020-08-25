# Generated by Django 2.2 on 2020-08-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviePoster', models.ImageField(upload_to='uploads/')),
                ('movieName', models.CharField(max_length=100)),
                ('movieDescription', models.TextField(blank=True)),
                ('createdDate', models.DateField(auto_now_add=True)),
                ('releaseDate', models.DateField()),
            ],
        ),
    ]