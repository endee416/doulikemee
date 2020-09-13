from django.urls import path
from . import views


urlpatterns=[
    path('', views.actualhome, name="actualhome"),
    path('login/',views.login, name='login'),
    path('login/hello/', views.hello, name='hello'),
    path('login/hello/home/', views.home, name='home'),
    path('login/hello/home/secondpage/', views.secondpage, name='secondpage'),
    path('login/hello/home/secondpage/thirdpage/', views.thirdpage, name='thirdpage'),
    path('login/hello/home/secondpage/thirdpage/fourthpage/', views.fourthpage, name='fourthpage'),
    path('login/hello/home/secondpage/thirdpage/fourthpage/report/', views.report, name='report'),
    path('login/hello/home/secondpage/thirdpage/fourthpage/fifthpage/', views.fifthpage, name='fifthpage')

]