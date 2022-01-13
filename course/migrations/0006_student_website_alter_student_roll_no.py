# Generated by Django 4.0.1 on 2022-01-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_remove_student_section_alter_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(unique=True),
        ),
    ]