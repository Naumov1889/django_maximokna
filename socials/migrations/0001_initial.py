# Generated by Django 2.2.6 on 2019-12-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=400)),
                ('icon', models.TextField(default=None, verbose_name='Иконка')),
                ('icon_larger', models.TextField(default=None, verbose_name='Иконка большего размера')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Сортировать')),
            ],
            options={
                'verbose_name': 'Соцсеть',
                'verbose_name_plural': 'Соцсети',
                'ordering': ['order'],
            },
        ),
    ]