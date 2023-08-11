from django.urls import path
from . import views



urlpatterns = [
    path('', views.CreateFeedBackView.as_view()),
    path('done/', views.DoneView.as_view()),
    path('update/<int:pk>/', views.UpdateFeedBackView.as_view()),
    path('list/', views.listFeedback.as_view()),
    path('detail/<int:pk>/', views.DetailFeedback.as_view()),
]
