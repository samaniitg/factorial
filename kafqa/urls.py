from django.contrib import admin
from django.urls import path
from .factorial_app.views import FindFactorial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/factorial/', FindFactorial.as_view(), name="find-factorial"),
]
