# Generated by Django 2.2.7 on 2020-03-22 09:18

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='pictures/')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(default='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=models.CharField(max_length=100, unique=True))),
                ('photographer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
