from django.urls import path
from . import views

urlpatterns = [
    # example route
    path('test/', views.test_view, name='test-view'),
]
