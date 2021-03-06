"""testpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from quiz import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',views.new_user,name="signin"),
    path('login/',views.login,name="login"),
    path('createquiz/',views.CreateQuizView.as_view(),name="create"),
    path('quizList/',views.QuizListView.as_view(),name="list"),
    path('createquestion/',views.CreateQuestionView.as_view(),name="createquestion"),
    url(r'^quizList/(?P<pk>[-\w]+)',views.QuizDetailView.as_view(),name="Detail"),
    path('menu/',views.Menu,name="menu"),
    path('quizstudentList/',views.QuizStudentListView.as_view(),name="studentlist"),
    url(r'^quizstudentList/(?P<pk>[-\w]+)',views.QuizStudentDetailView.as_view(),name="Detail"),
    url(r'',include("student.urls")),
]
