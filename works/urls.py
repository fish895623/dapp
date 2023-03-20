from django.urls import path
from .views import (
    TodoListApiView,
    WorksListApiView,
    WorkTitleListApiView,
    WorkStatusListApiView,
)

urlpatterns = [
    path("api/", TodoListApiView.as_view()),
    path("api/works", WorksListApiView.as_view()),
    path("api/worktitles", WorkTitleListApiView.as_view()),
    path("api/workstatuses", WorkStatusListApiView.as_view()),
]
