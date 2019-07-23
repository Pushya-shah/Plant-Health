from django.urls import path
from . import views

app_name="defect_demo"
urlpatterns = [
    path(' ', views.home, name='home'),
    path(" ", views.history,name='history'),
]
