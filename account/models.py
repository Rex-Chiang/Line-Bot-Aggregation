from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=64, unique=True)
    user_name = models.CharField(max_length=32)
    user_profile_pic = models.CharField(max_length=256, db_column="profile_pic")
    user_language = models.CharField(max_length=10, default=None)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user_name}-{self.user_id}"

    class Meta:
        db_table = "account"