# Generated by Django 4.2.7 on 2023-11-04 09:11

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('Title', models.CharField(max_length=50)),
                ('Excert', models.CharField(max_length=250)),
                ('Imagename', models.CharField(max_length=50)),
                ('Date', models.CharField(max_length=50)),
                ('Slug', models.SlugField(primary_key=True, serialize=False)),
                ('Content', models.TextField(blank=True, null=True)),
                ('Author', models.ForeignKey(default='No Author', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='author_query', to='blog.author')),
                ('Caption', models.ManyToManyField(related_name='lol', to='blog.tag')),
            ],
        ),
    ]