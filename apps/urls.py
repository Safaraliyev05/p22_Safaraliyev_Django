from django.contrib.auth.views import LoginView
from django.urls import path

from apps.views import RegisterCreateView, ProductListView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('', LoginView.as_view(
        template_name='apps/login.html',
        redirect_authenticated_user=True,
        next_page='products'
    ), name='login_page'),
    path('register/', RegisterCreateView.as_view(), name='register'),
]
