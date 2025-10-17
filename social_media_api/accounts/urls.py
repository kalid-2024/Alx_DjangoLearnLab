from django import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('register/', RegisterViw.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
]