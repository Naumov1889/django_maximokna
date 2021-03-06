# Generated by Django 2.2.6 on 2019-12-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstScreenImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablet', models.ImageField(default='bg-first-screen.jpg', upload_to='', verbose_name='Для планшета (от 500px до 1250px)')),
                ('mobile', models.ImageField(default='bg-first-screen-mobile.jpg', upload_to='', verbose_name='Для мобильных (до 500px)')),
            ],
            options={
                'verbose_name': 'Картинка для первого экрана главной страницы',
                'verbose_name_plural': 'Картинка для первого экрана главной страницы',
            },
        ),
    ]
