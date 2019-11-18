# Generated by Django 2.0.6 on 2018-06-18 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uiquery', '0004_auto_20180618_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='typeOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='query',
            name='searchEngine',
        ),
        migrations.RemoveField(
            model_name='randomisationorder',
            name='participant',
        ),
        migrations.RemoveField(
            model_name='result',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='result',
            name='preview',
        ),
        migrations.RemoveField(
            model_name='result',
            name='title',
        ),
        migrations.AddField(
            model_name='result',
            name='engine',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='result',
            name='html',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interviewsession',
            name='email',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='interviewsession',
            name='organisationPart',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='interviewsession',
            name='randomOrder',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='uiquery.typeOrder'),
            preserve_default=False,
        ),
    ]