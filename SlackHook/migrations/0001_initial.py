# Generated by Django 2.1.3 on 2018-11-16 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=255)),
                ('channel_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger_word', models.CharField(max_length=255)),
                ('text', models.TextField(null=True)),
                ('timestamp', models.DateTimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SlackHook.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slack_id', models.CharField(max_length=255)),
                ('slack_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='slack_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SlackHook.SlackUser'),
        ),
    ]
