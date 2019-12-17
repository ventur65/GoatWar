from django.urls import path

from . import views

app_name = 'backend'
urlpatterns = [
	path('index', views.index, name='index'),
	path('detail/<int:pk>', views.GoatDetailView.as_view(), name='goat_detail'),
	#path('vote/<int:winner_id>/<int:loser_id>/', views.vote, name='vote'),
]
