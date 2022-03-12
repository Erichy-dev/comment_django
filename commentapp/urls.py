from django.urls import path
from . import views

app_name = 'commentapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name ='index'),
    path('<int:pk>/', views.MyCommentView.as_view(), name='myComment')
]
