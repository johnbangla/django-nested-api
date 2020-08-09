from django.urls import path
from . import views
#from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('listings/', views.taskList, name="listings"),
    path('categories/', views.categoryList, name="categories"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
  #	path('auth/', obtain_jwt_token),
]
