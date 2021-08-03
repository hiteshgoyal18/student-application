from . import views
from django.urls import include,path



urlpatterns = [
	path('', views.index, name='student'),
	path('add', views.StudentCreateView.as_view(), name='add_student'),
	path('<int:pk>/update', views.StudentUpdateView.as_view(), name='update_student'),
]