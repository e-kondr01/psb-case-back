from django.urls import path

from .views import ProjectDetailView, ProjectListView

urlpatterns = [
    path("", ProjectListView.as_view()),
    path("/<int:pk>", ProjectDetailView.as_view()),
]
