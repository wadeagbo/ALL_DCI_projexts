# Generated by Django 3.2.3 on 2023-02-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('mac', models.IntegerField()),
                ('iph', models.IntegerField()),
                ('android', models.IntegerField()),
                ('oth', models.IntegerField()),
            ],
        ),
    ]
