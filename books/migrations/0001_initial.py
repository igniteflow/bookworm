# Generated by Django 2.0.2 on 2018-03-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(choices=[('action', 'Action'), ('adventure', 'Adventure'), ('romance', 'Romance'), ('fiction', 'Fiction'), ('fantasy', 'Fantasy'), ('non-fiction', 'Non Fiction'), ('science-fiction', 'Science Fiction'), ('satire', 'Satire'), ('drama', 'Drama'), ('mystery', 'Mystery'), ('poetry', 'Poetry'), ('comics', 'Comics'), ('horror', 'Horror'), ('art', 'Art'), ('diaries', 'Diaries'), ('guide', 'Guide'), ('travel', 'Travel')], default='action', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('published_date', models.DateField(blank=True)),
                ('authors', models.ManyToManyField(blank=True, related_name='_book_authors_+', to='books.Author', verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ReadingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('date_read', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='books.Book', verbose_name='book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='books.Publisher', verbose_name='publisher'),
        ),
    ]
