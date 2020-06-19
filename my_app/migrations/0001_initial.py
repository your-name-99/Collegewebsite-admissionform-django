# Generated by Django 3.0.3 on 2020-02-11 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('course', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('hobbies', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
