from django.urls import path
from manager.views import TaskManagerView


urlpatterns = [
    path('', TaskManagerView.as_view()),
]
