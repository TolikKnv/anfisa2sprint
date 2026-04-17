from django.urls import path

from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.proposal, name='create'),
    # path('accepted/', views.accepted, name='accepted'),
]