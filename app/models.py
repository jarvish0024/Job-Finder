
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.BigIntegerField(null=True)
    password = models.CharField(max_length=50)
    resume = models.FileField(upload_to='file')

    def __str__(self):
        return self.username

class Post_job(models.Model):
    company_name = models.CharField(max_length=30)
    company_post = models.CharField(max_length=30)
    job_mode = models.CharField(max_length=30)
    job_description = models.TextField(null=True)
    email = models.EmailField(max_length=50)
    work_hours = models.IntegerField(default=6)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    from_salary = models.IntegerField(default=1000)
    to_salary = models.IntegerField(default=5000)
    date = models.DateTimeField(default=True)

    def __str__(self):
        return str(self.id)

class Applied(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    contact = models.BigIntegerField(null=True)
    previous_company_name = models.CharField(max_length=100)
    education = models.CharField(max_length=30)
    experience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='file')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applied = models.ForeignKey(Post_job, on_delete=models.CASCADE)
    # date = models.DateTimeField(default=True)

    def __str__(self):
        return self.full_name