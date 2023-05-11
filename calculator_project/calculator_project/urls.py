from django.urls import path
from calculator_app.views import calculator

urlpatterns = [
    path('', calculator, name='calculator')
]