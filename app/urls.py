from operator import index
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('AddNote',views.AddNote,name='AddNote'),
    path('deleteTodo<int:id>',views.deleteTodo,name='deleteTodo'),
    path('change-status<int:id><str:status>',views.change_todo,name='change_todo'),
    path('logout',views.signout,name='signout')
]