# Generated by Django 4.2.7 on 2023-11-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=200)),
                ('companyName', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', max_length=15000, null=True)),
                ('cvFile', models.FileField(upload_to='cvFiles')),
                ('coverLetterFile', models.FileField(upload_to='clFiles')),
                ('applicationDate', models.DateField(auto_now_add=True)),
                ('gotFeedback', models.BooleanField(default=False)),
            ],
        ),
    ]
