# Generated by Django 3.1.7 on 2021-03-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AddField(
            model_name='task',
            name='extra_info',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=115),
        ),
    ]
