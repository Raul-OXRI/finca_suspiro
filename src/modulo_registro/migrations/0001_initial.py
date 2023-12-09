# Generated by Django 4.2.6 on 2023-12-09 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_animal', models.IntegerField()),
                ('codigo', models.IntegerField()),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('genero', models.CharField(choices=[('vaca', 'Vaca'), ('toro', 'Toro')], max_length=16)),
                ('edad', models.IntegerField()),
                ('partos', models.IntegerField()),
                ('desendencia', models.IntegerField()),
                ('observaciones', models.TextField(blank=True)),
            ],
        ),
    ]