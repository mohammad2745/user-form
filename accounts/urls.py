from django.urls import path
from .views import SignupView
urlpatterns = [
    path('accounts/', SignupView.as_view(), name='signin')
]
