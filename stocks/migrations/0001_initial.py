# Generated by Django 2.2.1 on 2019-05-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=100)),
                ('lName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('ZipCode', models.IntegerField()),
                ('phoneNo', models.IntegerField()),
                ('creditCard', models.IntegerField()),
            ],
        ),
    ]
