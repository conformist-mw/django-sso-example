from django.urls import path

from .views import SignUpView, index

urlpatterns = [
    path('auth/signup/', SignUpView.as_view(), name='signup'),
    path('', index, name='index'),
]
