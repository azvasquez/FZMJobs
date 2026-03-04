from django.db import models

# Create your models here.

class JobApplication(models.Model):
    class Status(models.TextChoices):
        SAVED = 'saved', 'Saved'
        APPLIED = 'applied', 'Applied'
        UNDER_REVIEW = 'under review', 'Under Review'
        REJECTED_PRESCREEN = 'rejected after prescreen', 'Rejected After Prescreen'
        INTERVIEWING = 'interviewing', 'Interviewing'
        REJECTED_POSTINTERVIEW = 'rejected after interview', 'Rejected After Interview'
        RECEIVED_OFFER = 'received offer', 'Received Offer'
        OTHER = 'other', 'Other'


    role_title = models.CharField()
    company = models.CharField()
    url = models.URLField()
    job_description = models.TextField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.INVALID)
    date_applied = models.DateTimeField(null=True, blank=True)
    next_step_due = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.role_title} at {self.company}'

class HealthStatus(models.TextChoices):
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
