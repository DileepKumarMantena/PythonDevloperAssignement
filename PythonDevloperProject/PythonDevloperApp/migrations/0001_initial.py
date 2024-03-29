# Generated by Django 5.0.3 on 2024-03-18 16:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='titlemust string and should not be less than 3 and greater than 12', regex='^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Author', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(message='lastname must string and should not be less than 3 and greater than 12', regex='^(?=.{3,12}$)(?![_.])(?!.*[_.]{2})[a-zA-Z]+(?<![_.])$')])),
                ('Date_Field', models.DateField(validators=[django.core.validators.RegexValidator(message='Date must be in the format YYYY-MM-DD', regex='^\\d{4}-\\d{2}-\\d{2}$')])),
            ],
            options={
                'db_table': 'Books_Table',
            },
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Review_Text', models.TextField(validators=[django.core.validators.MinLengthValidator(50, message='Review must be at least 50 characters long.'), django.core.validators.MaxLengthValidator(1000, message='Review cannot exceed 1000 characters.')])),
                ('Rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Integer must be greater than or equal to 0.'), django.core.validators.MaxValueValidator(100, message='Integer must be less than or equal to 100.')])),
                ('BookId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookId', to='PythonDevloperApp.booksmodel')),
            ],
            options={
                'db_table': 'Review_Table',
            },
        ),
    ]
