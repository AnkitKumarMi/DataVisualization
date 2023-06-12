from django.contrib import admin
from django.urls import path
from WebApp import views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.HomeView.as_view()),
	# path('test-api', views.get_data),
	path('api', views.ChartData.as_view()),
]
