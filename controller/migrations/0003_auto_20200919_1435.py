# Generated by Django 2.2 on 2020-09-19 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controller', '0002_auto_20200917_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designaiton', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Raw_Materials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rm', models.CharField(max_length=100, verbose_name='Raw Materials')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='CContact',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='CName',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='CProfile_Image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email_confirmed',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='Company_name',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='VContact',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='VName',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='VProfile_Image',
        ),
        migrations.RemoveField(
            model_name='vendors',
            name='email_confirmed',
        ),
        migrations.AddField(
            model_name='customer',
            name='caddress',
            field=models.CharField(blank=True, max_length=500, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='customer',
            name='ccontact',
            field=models.CharField(blank=True, default='N/A', max_length=20, verbose_name='Contact'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cemail_confirmed',
            field=models.BooleanField(default=False, verbose_name='Email Confirmation'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cgender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='customer',
            name='cprofile_Image',
            field=models.ImageField(blank=True, default='https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', upload_to='Customer_Profile_Pic/', verbose_name='Profile Image'),
        ),
        migrations.AddField(
            model_name='customer',
            name='institution_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='Instituion ID'),
        ),
        migrations.AddField(
            model_name='customer',
            name='institution_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Instituion Name'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='company_id',
            field=models.CharField(blank=True, max_length=200, verbose_name='Company ID'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Company Name'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='vaddress',
            field=models.CharField(blank=True, max_length=500, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='vcontact',
            field=models.CharField(blank=True, default='N/A', max_length=20, verbose_name='Contact'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='vemail_confirmed',
            field=models.BooleanField(default=False, verbose_name='Email Confirmation'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='vgender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='vendors',
            name='vprofile_Image',
            field=models.ImageField(blank=True, default='https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', upload_to='Vendor_Profile_Pic/', verbose_name='Profile Image'),
        ),
        migrations.CreateModel(
            name='Company_Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_No', models.CharField(blank=True, max_length=200, verbose_name='Card No.')),
                ('eaddress', models.CharField(blank=True, max_length=500, verbose_name='Address')),
                ('econtact', models.CharField(blank=True, default='N/A', max_length=20, verbose_name='Contact')),
                ('eprofile_Image', models.ImageField(blank=True, default='https://icon-library.net/images/young-person-icon/young-person-icon-7.jpg', upload_to='Employee_Profile_Pic/', verbose_name='Profile Image')),
                ('egender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=2, verbose_name='Gender')),
                ('eemail_confirmed', models.BooleanField(default=False, verbose_name='Email Confirmation')),
                ('Updated_at', models.DateTimeField(auto_now=True)),
                ('designation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='controller.Designation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
