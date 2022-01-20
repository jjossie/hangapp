# Generated by Django 4.0.1 on 2022-01-20 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hangapp', '0003_remove_option_usersvoted_remove_session_users_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='session',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='hangapp.user'),
        ),
    ]