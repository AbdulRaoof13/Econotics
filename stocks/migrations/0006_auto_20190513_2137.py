# Generated by Django 2.2.1 on 2019-05-13 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stocks', '0005_auto_20190512_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=100)),
                ('ZipCode', models.CharField(max_length=12)),
                ('phoneNo', models.CharField(max_length=100)),
                ('creditCard', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
