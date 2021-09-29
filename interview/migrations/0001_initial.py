# Generated by Django 2.2.5 on 2020-02-26 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Degree',
                'db_table': 'Degree',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(help_text='Provide  valid Email-Id', max_length=254)),
                ('contact', models.CharField(help_text='Enter mobile number', max_length=10)),
                ('address', models.TextField(help_text='Provide current address')),
                ('qualification', models.ForeignKey(help_text='select a highest qualification you have done', on_delete=django.db.models.deletion.CASCADE, to='interview.Degree')),
            ],
            options={
                'verbose_name_plural': 'Employee',
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='Interview_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_done', models.BooleanField(default=True)),
                ('review', models.CharField(blank=True, choices=[('Good', 'Good'), ('Bad', 'Bad'), ('Average', 'Average')], max_length=15, verbose_name='If Interview is done, then Please select')),
                ('status', models.CharField(blank=True, choices=[('Postponed', 'Postponed'), ('Canceled', 'Canceled')], max_length=15, verbose_name='If interview is not done then select')),
            ],
            options={
                'verbose_name_plural': 'Interview_Done',
                'db_table': 'Interview_Done',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Subject',
                'db_table': 'Subject',
            },
        ),
        migrations.CreateModel(
            name='Schedule_Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_interview', models.DateTimeField()),
                ('venue', models.TextField()),
                ('role', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('candidate_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Schedule_Interview',
                'db_table': 'Schedule_Interview',
            },
        ),
        migrations.CreateModel(
            name='Salary_Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('bank_name', models.CharField(max_length=25)),
                ('account_no', models.CharField(max_length=15)),
                ('ifsc', models.CharField(max_length=10)),
                ('date', models.DateField(help_text='Date of Salary')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Salary_Account',
                'db_table': 'Salary_Account',
            },
        ),
        migrations.CreateModel(
            name='Resignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(help_text='please mention the years/months whatever you have completed', max_length=25)),
                ('reason', models.TextField()),
                ('Feedback', models.TextField()),
                ('date', models.DateField(help_text='Date of Resignation must be 1 month later from now')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Resignation',
                'db_table': 'Resignation',
            },
        ),
        migrations.CreateModel(
            name='Project_Allocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_description', models.TextField()),
                ('language', models.CharField(help_text='c++,java,python,PHP, etc...', max_length=60)),
                ('daily_tasks', models.CharField(help_text='total no of tasks to complete daily', max_length=5)),
                ('expected_completion_time', models.CharField(help_text='in hrs', max_length=5)),
                ('personal_guide', models.CharField(help_text='you can take a help of this person for any queries', max_length=20)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Project_Allocation',
                'db_table': 'Project_Allocation',
            },
        ),
        migrations.CreateModel(
            name='Offer_Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=10)),
                ('joining_date', models.DateField()),
                ('entry_time', models.TimeField()),
                ('exit_time', models.TimeField()),
                ('benefits', models.TextField()),
                ('company_name', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=50)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Offer_Letter',
                'db_table': 'Offer_Letter',
            },
        ),
        migrations.CreateModel(
            name='Leave_Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('total', models.IntegerField(help_text='total no of days for leave')),
                ('reason', models.TextField(blank=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Leave_Management',
                'db_table': 'Leave_Management',
            },
        ),
        migrations.CreateModel(
            name='Experiance_Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('total_experiance', models.FloatField(help_text='in years')),
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('progress', models.TextField(help_text='In short review about the employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Experiance_Letter',
                'db_table': 'Experiance_Letter',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='specialization',
            field=models.ForeignKey(help_text='select a subject of specialization', on_delete=django.db.models.deletion.CASCADE, to='interview.Subject'),
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssc_marklist', models.FileField(upload_to='')),
                ('hsc_marklist', models.FileField(upload_to='')),
                ('adhar_card', models.FileField(upload_to='')),
                ('pancard', models.FileField(blank=True, upload_to='')),
                ('photo', models.ImageField(upload_to='')),
                ('address_proof', models.FileField(upload_to='')),
                ('experiance_letter', models.FileField(blank=True, help_text='If fresher, no need to attach this file', upload_to='')),
                ('salary_slip', models.FileField(blank=True, help_text='If fresher, no need to attach this file', upload_to='')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Documents',
                'db_table': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=50, verbose_name='Select the month')),
                ('present_days', models.IntegerField()),
                ('absent_days', models.IntegerField()),
                ('total_holidays', models.IntegerField()),
                ('total_days', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Attendance',
                'db_table': 'Attendance',
            },
        ),
        migrations.CreateModel(
            name='Account_Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desk', models.CharField(max_length=5)),
                ('machine', models.CharField(max_length=5)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Employee')),
            ],
            options={
                'verbose_name_plural': 'Account_Setup',
                'db_table': 'Account_Setup',
            },
        ),
    ]
