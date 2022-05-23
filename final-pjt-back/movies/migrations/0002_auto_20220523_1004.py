# Generated by Django 3.2.12 on 2022-05-23 01:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genres',
            new_name='genre_ids',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='casts',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='crews',
        ),
        migrations.AddField(
            model_name='cast',
            name='character',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='cast',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AddField(
            model_name='crew',
            name='job',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='crew',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie'),
        ),
        migrations.AddField(
            model_name='movie',
            name='vote_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='crew',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='movie',
            name='popularity',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('movie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]
