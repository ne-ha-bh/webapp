# Generated by Django 2.2 on 2020-05-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=5)),
                ('ename', models.CharField(max_length=5)),
                ('eemail', models.EmailField(max_length=254)),
                ('ephnone_no', models.CharField(max_length=15)),
            ],
        ),
    ]
