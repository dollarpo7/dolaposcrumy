# Generated by Django 2.0.2 on 2018-03-17 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dolaposcrumy', '0003_auto_20180317_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrumygoals',
            name='status_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dolaposcrumy.ScrumyStatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='task_category',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dolaposcrumy.ScrumyUser'),
            preserve_default=False,
        ),
    ]
