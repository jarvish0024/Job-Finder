from django.contrib import admin
from app.models import Customer, Post_job, Applied

# Register your models here.

@admin.register(Customer)                     # to register model with fields in admin panel
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'resume']

@admin.register(Post_job) 
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'company_post', 'job_mode', 'job_description', 'email', 'work_hours', 'country', "state", "from_salary", 'to_salary', 'date']

@admin.register(Applied)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'contact', 'previous_company_name', 'education', 'experience', 'resume']