# feedback/urls.py
from django.urls import path
from .views import feedback_view, thanks_view

app_name = 'app1'

urlpatterns = [
    path('', feedback_view, name='feedback_form'),
    path('thanks/', thanks_view, name='thanks'),
]
