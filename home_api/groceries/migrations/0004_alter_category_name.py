# Generated by Django 4.1.3 on 2022-11-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0003_auto_20221107_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Vegetables', 'Vegetables'), ('Fruit', 'Fruit')], max_length=20, primary_key=True, serialize=False),
        ),
    ]
