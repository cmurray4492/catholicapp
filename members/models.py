"""Model file for the Members App"""
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce import HTMLField
import uuid


class Members(models.Model):
    """Members Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    member_first_name = models.CharField(max_length=100)
    member_last_name = models.CharField(max_length=100)
    member_email_address = models.EmailField()
    member_image = models.ImageField(upload_to='photos/%Y/%m/%d/', default="")
    member_bio = HTMLField(blank=True)
    member_date_joined = models.DateTimeField(default=datetime.now, blank=True)
    member_is_active = models.BooleanField(blank=True, default=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.member_email_address
