from django.db import models

# Create your models here.

class JobApplication(models.Model):
    role_title = models.CharField()
    company = models.CharField()
    url = models.URLField()
    job_description = models.TextField()
    notes = models.TextField(blank=True)
    status = models.CharField(choices={
        'SAVED': 'saved',
        'APPLIED': 'applied',
        'DENIED': 'denied',
        'INTERVIEWING': 'interviewing',
        'UNDER REVIEW': 'under review',
        'RECEIVED OFFER': 'received offer',
    })
    date_applied = models.DateTimeField(null=True, blank=True)
    next_step_due = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.role_title} at {self.company}'

