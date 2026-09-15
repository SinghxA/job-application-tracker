from django.db import models

# Create your models here.

class JobApplication(models.Model):
    company_name=models.CharField(max_length=90)
    role=models.CharField(max_length=70)
    date_applied=models.DateField()
    job_domain=models.CharField(max_length=70)
    status = models.CharField(
    max_length=20,
    choices=[
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer' , 'Offer'),
        ('rejected'  ,'Rejected'),
    ]
)
    

   
