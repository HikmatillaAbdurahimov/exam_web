from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
import requests
from django.views.generic import FormView
from .forms import LoginModelForm
from django.contrib.auth import authenticate,login


class HomeView(View):
    def get(self,request):
        teachers = requests.get("http://127.0.0.1:8000/api/teacher-web//").json()
        courses = requests.get("http://127.0.0.1:8000/api/course-web//").json()
        course_moduls = requests.get("http://127.0.0.1:8000/api/coursemodul-web//").json()
        students = requests.get("http://127.0.0.1:8000/api/student-web//").json()
        student_comments = requests.get("http://127.0.0.1:8000/api/student-comment-web//").json()
        questions = requests.get("http://127.0.0.1:8000/api/questions-web//").json()

        context = {
            "teachers": teachers,
            "courses":courses,
            "course_moduls":course_moduls,
            "students":students,
            "student_comments":student_comments,
            "questions":questions
        }
        return render(request,'index.html',context)

class Courses(View):
    def get(self,request):
        courses = requests.get("http://127.0.0.1:8000/api/course-web//").json()
        context = {
            "courses": courses}
        return render(request, 'blog.html', context)

class CoursesModel(View):
    def get(self,request):
        course_moduls = requests.get("http://127.0.0.1:8000/api/coursemodul-web//").json()
        context = {
            "course_moduls": course_moduls}
        return render(request, 'service.html', context)


class Teacher(View):
    def get(self,request):
        teachers = requests.get("http://127.0.0.1:8000/api/teacher-web//").json()
        context = {
            "teachers": teachers}
        return render(request, 'team.html', context)


class Student(View):
    def get(self,request):
        student_comments = requests.get("http://127.0.0.1:8000/api/student-comment-web//").json()
        context = {
            "student_comments":student_comments }
        return render(request, 'testimonial.html', context)





#
# class Teacher(View):
#     def get(self,request):
#         teachers = requests.get("http://127.0.0.1:8000/api/teacher-web//").json()
#         context={
#             "teachers":teachers
#         }
#         return render(request,'about.html',context)
#
#
# class Course(View):
#     def get(self,request):
#         courses = requests.get("http://127.0.0.1:8000/api/course-web//").json()
#         context={
#             "courses":courses
#         }
#         return render(request,'service.html',context)
#
#
# class CourseModuls(View):
#     def get(self,request):
#         course_moduls = requests.get("http://127.0.0.1:8000/api/coursemodul-web//").json()
#         context={
#             "course_moduls":course_moduls
#         }
#         return render(request,'blog.html',context)
#










def home_view(request):
    return render(request, 'index.html')

def FAQ_view(request):
    return render(request, 'FAQ.html')

def blog_view(request):
    return render(request, 'blog.html')

def contact_view(request):
    return render(request, 'contact.html')


def feature_view(request):
    return render(request, 'feature.html')


def offer_view(request):
    return render(request, 'offer.html')


def service_view(request):
    return render(request, 'service.html')


def team_view(request):
    return render(request, 'team.html')

def testimonial_view(request):
    return render(request, 'testimonial.html')


def about_view(request):
    return render(request,'about.html')