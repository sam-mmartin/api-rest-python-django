# Generated by Django 5.0.6 on 2024-05-09 16:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('start_date_use', models.DateField()),
                ('level', models.CharField(choices=[('B', 'Básico'), ('I', 'Intermediário'), ('A', 'Avançado')], default='B', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('work', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_api.language')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_api.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='languages',
            field=models.ManyToManyField(through='site_api.UserLanguage', to='site_api.language'),
        ),
        migrations.CreateModel(
            name='UserSocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_api.social')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_api.user')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='socials_medias',
            field=models.ManyToManyField(through='site_api.UserSocialMedia', to='site_api.social'),
        ),
    ]
