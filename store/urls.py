from django.urls import path
from .models import *
from .views import *


urlpatterns = [
    path('', CarViewSet.as_view({'get':'list', 'post':'create'})),
    path('<int:pk>/', CarViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy'}))

]