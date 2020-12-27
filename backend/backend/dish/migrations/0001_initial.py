# Generated by Django 2.2 on 2020-12-22 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('label', models.CharField(max_length=120)),
                ('image', models.FileField(upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('featured', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
    ]
