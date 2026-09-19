from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JobApplication(models.Model):
    company_name=models.CharField(max_length=90)
    role=models.CharField(max_length=70)
    date_applied=models.DateField()
    
    status = models.CharField(
    max_length=20,
    choices=[
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer' , 'Offer'),
        ('rejected'  ,'Rejected'),
    ]
)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
    

   
