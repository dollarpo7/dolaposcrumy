# Generated by Django 2.0.2 on 2018-03-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dolaposcrumy', '0004_auto_20180317_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumystatus',
            name='status',
            field=models.CharField(choices=[('WT', 'Weekly Task'), ('DT', 'Daily Task'), ('V', 'Verified'), ('D', 'Done')], max_length=50),
        ),
    ]
