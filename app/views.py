from multiprocessing import context
from django.shortcuts import render, redirect
from app.models import Customer, Post_job, Applied
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'index.html')

def find_job(request):
    job_list = Post_job.objects.all()
    context = {'job_list':job_list}
    return render(request, 'job_listing.html', context)

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')

def submit_job(request):
    if request.method=='POST':
        company_name = request.POST.get('companyname')
        post = request.POST.get('post')
        jobmode = request.POST.get('jobmode')
        description = request.POST.get('job_description')
        email = request.POST.get('email')
        time = request.POST.get('time')
        country = request.POST.get('country')
        state = request.POST.get('state')
        f_salary = request.POST.get('from_salary')
        t_salary = request.POST.get('to_salary')
        date = request.POST.get('date')
        Post_job.objects.create(company_name=company_name, company_post=post, job_mode=jobmode, job_description=description, email=email, work_hours=time, country=country, state=state, from_salary=f_salary, to_salary=t_salary, date=date)
        return redirect('/job_list/')
    return render(request, 'application.html')

def register(request):
    if request.method=='POST':
        username = request.POST.get('username')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User.objects.create_user(username=username,first_name=f_name,last_name=l_name,email=email,password=password)
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.POST.get('resume')
        Customer.objects.create(user=user,first_name=f_name, last_name=l_name, email=email, phone=phone, resume=resume)
        return redirect('/login/')
    return render(request, 'register.html')

def user_login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html')
    return render(request, 'login.html')

def show_applied(request):
    user=request.user
    list=Applied.objects.filter(user_id=user)
    context={'list':list}
    return render(request, 'appliedjobs.html', context)

def job_apply(request, pk):
    applied_jobs = Post_job.objects.get(id=pk)
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        com_name=request.POST.get('prev-company-name')
        education=request.POST.get('edu')
        experience=request.POST.get('experience')
        resume=request.POST.get('resume')
        Applied.objects.create(user=request.user, applied=applied_jobs, full_name=fullname, email=email, contact=phone, previous_company_name=com_name, education=education, experience=experience, resume=resume)
        return redirect('/appliedjobs')
    return render(request, 'job_apply.html')

def changepassword(request):
    return render(request, 'changepassword.html')

def job_details(request, pk):
    print(pk)
    jobs = Post_job.objects.get(id=pk)
    print(jobs)
    context = {'jobs':jobs}
    return render(request, 'job_details.html',context)

def applied_job_details(request, pk):
    print(pk)
    jobs = Post_job.objects.get(id=pk)
    print(jobs)
    context = {'jobs':jobs}
    return render(request, 'applied_job_details.html',context)

def profile(request):
    cos=Customer.objects.all()
    context = {'cos':cos}
    return render(request, 'profile.html',context)
