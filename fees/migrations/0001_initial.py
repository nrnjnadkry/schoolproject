# Generated by Django 4.0.1 on 2022-01-10 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeeStructure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=150)),
                ('grade', models.IntegerField()),
                ('department', models.CharField(max_length=150)),
                ('lastResult', models.FloatField()),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]