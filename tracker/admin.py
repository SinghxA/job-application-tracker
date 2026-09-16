from django.contrib import admin

# Register your models here.
from .models import JobApplication

@admin.register(JobApplication)
# Django ka ready-made Admin
#         ↓
#    ModelAdmin
#         ↓
# Hum apni customization add karte hain
 
class JobApplicationAdmin(admin.ModelAdmin):
    # Hum admin panel ke appearance/behavior ko customize kar rahe hain.
    list_display = ('company_name', 'role', 'date_applied', 'job_domain', 'status')

    search_fields = ('company_name', 'role', 'job_domain')
    list_filter = ('status',)
    date_hierarchy = 'date_applied'
    
    
