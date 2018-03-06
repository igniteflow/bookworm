# Generated by Django 2.0.2 on 2018-03-06 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180305_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='books.Publisher', verbose_name='publisher'),
        ),
        migrations.AlterField(
            model_name='readinglist',
            name='book',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='books.Book', verbose_name='book'),
        ),
        migrations.AlterField(
            model_name='readinglist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]