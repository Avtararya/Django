# Generated by Django 3.2.21 on 2023-09-08 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0002_auto_20230822_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('genre', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('age', models.PositiveIntegerField()),
                ('annual_income', models.PositiveIntegerField()),
                ('spending_score', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Invoice',
        ),
    ]