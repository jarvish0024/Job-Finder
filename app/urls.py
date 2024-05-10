from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',views.home, name='home'),
    path('job_list/',views.find_job, name='job_list'),
    path('profile/', views.profile, name='profile'),
    path('about/',views.about, name='about'),
    path('contact_us/',views.contact_us, name='contact'),
    path('submit_job/',views.submit_job, name='application'),
    path('register/',views.register, name='register'),
    path('login/',views.user_login, name='login'),
    path('appliedjobs/',views.show_applied, name='appliedjobs'),
    path('changepassword/',views.changepassword, name='changepassword'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'), # django inbuilt logout only url needed
    path('job_details/<int:pk>',views.job_details, name='job_details'),
    path('applied_job_details/<int:pk>', views.applied_job_details, name='applied_job_details'),
    path('job_apply/<int:pk>',views.job_apply, name='job_apply'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # to show  image in frontend
