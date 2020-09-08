from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=107)
    phone_number = models.CharField(max_length=13)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return "[" + ",".join((str(self.id), self.email, self.name, self.phone_number, str(self.is_verified))) + "]"


class Verification(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=60)
    otp = models.CharField(max_length=6)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(blank=True, default=timezone.now)

    # def __init__(self, email, otp, user, created_at):
    #     super(Verification, self).__init__()
    #     # models.Model.__init__(self)
    #     self.email = email
    #     self.otp = otp
    #     self.user = user
    #     self.created_at = created_at

    def __str__(self):
        return self.email


class Login(models.Model):
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=107)

    def __str__(self):
        return self.email

