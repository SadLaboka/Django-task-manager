from django.views.generic import TemplateView


class TaskManagerView(TemplateView):
    """View for main page"""
    template_name = 'manager/task_manager.html'
