# Generated by Django 4.2 on 2023-09-29 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=45)),
                ('Phone', models.IntegerField()),
                ('Address', models.CharField(max_length=55)),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'signtb',
            },
        ),
    ]
