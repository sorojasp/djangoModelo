from profiles_app import views
from django.urls import include, path

urlpatterns = [
    path('hello-view/', views.HelloView.as_view()),
]


