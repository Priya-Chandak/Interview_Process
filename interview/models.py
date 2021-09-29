from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Degree(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
       return self.name

    class Meta:
        db_table = 'Degree'
        verbose_name_plural='Degree'

class Subject(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Subject'
        verbose_name_plural='Subject'

class Employee(models.Model):
    first_name =models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(help_text='Provide  valid Email-Id')
    contact=models.CharField(max_length=10, help_text='Enter mobile number')
    address=models.TextField(help_text='Provide current address')
    qualification=models.ForeignKey(Degree,on_delete=models.CASCADE, help_text='select a highest qualification you have done')
    specialization=models.ForeignKey(Subject,on_delete=models.CASCADE, help_text='select a subject of specialization')

    class Meta:
        db_table = 'Employee'
        verbose_name_plural='Employee'

    def __str__(self):
        return "%s %s" % (self.first_name,self.last_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)


class Schedule_Interview(models.Model):
    employee=models.ManyToManyField(Employee)
    # candidate_name=models.ForeignKey(Employee ,on_delete=models.CASCADE)
    date_of_interview=models.DateTimeField()
    venue=models.TextField()
    role=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)

    class Meta:
        db_table = 'Schedule_Interview'
        verbose_name_plural='Schedule_Interview'

    def __str__(self):
        return self.role


class Interview_Status(models.Model):
    is_done=models.BooleanField(default=True)

    Good = 'Good'
    Bad = 'Bad'
    Average = 'Average'
 
    Review_choices = (
        (Good, 'Good'),
        (Bad, 'Bad'),
        (Average, 'Average')
    )   
 
    review = models.CharField('If Interview is done, then Please select', max_length=15, choices=Review_choices,blank=True)

    Postponed='Postponed'
    Canceled='Canceled'

    status=(    
        (Postponed,'Postponed'),
        (Canceled,'Canceled')
    )

    status=models.CharField('If interview is not done then select',max_length=15,choices=status, blank=True)

    def __str__(self):
        return self.is_done

    class Meta:
        db_table='Interview_Done'
        verbose_name_plural='Interview_Done'

class Documents(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    ssc_marklist=models.FileField()
    hsc_marklist=models.FileField()
    adhar_card=models.FileField(blank=False)
    pancard=models.FileField(blank=True)
    photo=models.ImageField(blank=False)
    address_proof=models.FileField(blank=False)
    experiance_letter=models.FileField(help_text='If fresher, no need to attach this file',blank=True)
    salary_slip=models.FileField(help_text='If fresher, no need to attach this file',blank=True)

    class Meta:
        db_table='Documents'
        verbose_name_plural='Documents'


class Offer_Letter(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    position=models.CharField(max_length=50)
    salary=models.CharField(max_length=10)
    joining_date=models.DateField()
    entry_time=models.TimeField()
    exit_time=models.TimeField()
    benefits=models.TextField()
    company_name=models.CharField(max_length=20)
    venue=models.CharField(max_length=50)

    def _str__(self):
        return self.position
    
    class Meta:
        db_table='Offer_Letter'
        verbose_name_plural='Offer_Letter'


class Account_Setup(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    desk=models.CharField(max_length=5)
    machine=models.CharField(max_length=5)

    class Meta():
        db_table='Account_Setup'
        verbose_name_plural='Account_Setup'


class Project_Allocation(models.Model):
    Employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_name=models.CharField(max_length=50)
    project_description=models.TextField()
    language=models.CharField(max_length=60,help_text='c++,java,python,PHP, etc...')
    daily_tasks=models.CharField(max_length=5,help_text='total no of tasks to complete daily')
    expected_completion_time=models.CharField(max_length=5,help_text='in hrs')
    personal_guide=models.CharField(max_length=20,help_text='you can take a help of this person for any queries')


    class Meta():
        db_table='Project_Allocation'
        verbose_name_plural='Project_Allocation'

class Leave_Management(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    from_date=models.DateField()
    to_date=models.DateField()
    total=models.IntegerField(help_text='total no of days for leave')
    reason=models.TextField(blank=True)

    class Meta():
        db_table='Leave_Management'
        verbose_name_plural='Leave_Management'

class Salary_Account(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    amount=models.IntegerField()
    bank_name=models.CharField(max_length=25)
    account_no=models.CharField(max_length=15)
    ifsc=models.CharField(max_length=10)
    date=models.DateField(help_text='Date of Salary')

    class Meta():
        db_table='Salary_Account'
        verbose_name_plural='Salary_Account'

class Attendance(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)

    Jan='January'
    Feb='February'
    Mar='March'
    Apr='April'
    May='May'
    Jun='June'
    Jul='July'
    Aug='August'
    Sep='September'
    Oct='October'
    Nov='November'
    Dec='December'

    month=(    
        (Jan,'January'),
        (Feb,'February'),
        (Mar,'March'),
        (Apr,'April'),
        (May,'May'),
        (Jun,'June'),
        (Jul,'July'),
        (Aug,'August'),
        (Sep,'September'),
        (Oct,'October'),
        (Nov,'November'),
        (Dec,'December'),
    )

    month=models.CharField('Select the month',choices=month, max_length=50)
    present_days=models.IntegerField()
    absent_days=models.IntegerField()
    total_holidays=models.IntegerField()
    total_days=models.IntegerField()

    class Meta():
        db_table='Attendance'
        verbose_name_plural='Attendance'

class Resignation(models.Model):
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    duration=models.CharField(max_length=25,help_text='please mention the years/months whatever you have completed')
    reason=models.TextField()
    Feedback=models.TextField()
    date=models.DateField(help_text='Date of Resignation must be 1 month later from now')

    class Meta():
        db_table='Resignation'
        verbose_name_plural='Resignation'

class Experiance_Letter(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    position=models.CharField(max_length=30)
    total_experiance=models.FloatField(help_text='in years')
    salary=models.IntegerField()
    from_date=models.DateField()
    to_date=models.DateField()
    progress=models.TextField(help_text='In short review about the employee')

    class Meta():
        db_table='Experiance_Letter'
        verbose_name_plural='Experiance_Letter'
