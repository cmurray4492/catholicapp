"""Model file for the Members App"""
from django.db import models
from datetime import datetime
from tinymce import HTMLField


class Members(models.Model):
    """Members Model"""
    member_first_name = models.CharField(max_length=100)
    member_last_name = models.CharField(max_length=100)
    member_email_address = models.EmailField()
    member_image = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")
    member_bio = HTMLField(blank=True)
    member_date_joined = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.member_email_address
