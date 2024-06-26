# Generated by Django 4.2.11 on 2024-06-26 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='posters/')),
            ],
        ),
    ]
