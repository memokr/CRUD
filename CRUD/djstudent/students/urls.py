
from django.urls.conf import path,include
from . import views

urlpatterns = [
    path('form',views.student_form),
    path('list/',views.student_list)
]
