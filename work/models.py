from django.db import models

class WorkDetail(models.Model):
    link = models.TextField(max_length=255)

    WORK_TYPE_CHOICES = [
        ('YT', 'Youtube'),
        ('IM', 'Instagram'),
        ('OT', 'Other'),
    ]
    worke_type = models.CharField(
        choices=WORK_TYPE_CHOICES,
        default='OT',
        max_length=2
    )


