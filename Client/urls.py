from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.Welcome,name='home'),
    path('home/', views.Welcome,name='home'),
       

   # path('signup/' , views.client_signup , name='client-signup'),
    #path('chatbot/', views.client_chatbot , name='client-chatbot'),
    path('login_user/',views.login_user ,name='login'),
    path('chatbot/', views.ChatbotInterface, name='chatbot'),
    #path('about/', views.about, name='about')

]
