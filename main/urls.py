from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('education/', views.education, name='education'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('solutions/', views.solutions, name='solutions'),
    path('teaching/', views.teaching, name='teaching'),
    path('contact/', views.contact, name='contact'),
    path('resources/<int:topicid>', views.resources, name='resources'),
    path('books/<int:bookid>', views.books, name='books'),
    path('contact/sendmessage/', views.sendmessage, name='sendmessage'),
]
