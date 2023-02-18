from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .forms import MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
# from django.urls import path
# from app.views import popup
app_name ='app'
urlpatterns = [
   path('',views.home,name='home'),
   path('register/',views.register_attempt,name='register'),
   path('accounts/login/',views.login_attempt,name='login'),
   path('logout/',views.user_logout,name='logout'),
   path('token/',views.token_send,name='token_send'),
   path('success/',views.success,name='success'),
   path('verify/<auth_token>/',views.verify,name='verify'),
   path('error/',views.error_page,name='error'),
   path('details/',views.DetailView.as_view(),name='details'),
   # path('run/',views.runcode,name='run'),
   path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
   path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),
   path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_confirm'),
   path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),
   path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm),name='password_change'),
   path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
   path('enquiry/',views.Enquiry,name='enquiry'),
   path('success_page/',views.Success_page,name='success_page') ,
   # path('popup/',views.popup, name='popup')

 
   
]