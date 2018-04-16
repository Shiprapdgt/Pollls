from django.urls import path

from . import views

app_name = 'profile'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('translations/', views.my_view, name='my_view'),
    path('translationspage/', views.login, name='login'),
]