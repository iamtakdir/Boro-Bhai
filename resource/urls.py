from django.urls import path
from resource import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home , name= 'home'),
    path('dashboard', views.dashboard , name= 'dashboard'),
    #auth 
    path('signup',views.Signup.as_view(), name= 'signup'),
    path('login',auth_views.LoginView.as_view(), name= 'login'),
    path('logout',auth_views.LogoutView.as_view(), name= 'logout'),
    #Resource 
    path('resource/create',views.CreateSource.as_view() , name='create_source'),
    path('resource/<int:pk>',views.DetailSource.as_view() , name='detail_source'),
    path('resource/<int:pk>/update',views.UpdateSource.as_view() , name='update_source'),
    path('resource/<int:pk>/delete',views.DeleteSource.as_view() , name='delete_source'),

]
