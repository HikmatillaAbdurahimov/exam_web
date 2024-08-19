
from django.urls import path
from .views import home_view,FAQ_view,blog_view,contact_view,feature_view,offer_view,team_view,testimonial_view,service_view,about_view
from .views import HomeView,Courses,CoursesModel,Teacher,Student


urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('course/',Courses.as_view(),name='course'),
    path('course-model/',CoursesModel.as_view(),name='course-model'),
    path('team/',Teacher.as_view(),name='team'),
    path('student/',Student.as_view(),name='student'),


    path('contact/',contact_view,name='contact'),
    path('faq/',FAQ_view,name='faq'),
    path('team/',team_view,name='team'),
    path('testimonial/',testimonial_view,name='testimonial'),
    path('offer/',offer_view,name='offer'),
    path('feature/',feature_view,name='feature'),
]