from django.urls import path
from .views import main
from main_page.views import add_feedback, post_ajax_feedback, get_feedback_json

urlpatterns = [
    path('', main, name='main_page'),
    path('add_feedback/', add_feedback, name="add_feedback"),
    path('submit_feedback/', post_ajax_feedback, name="post_ajax_feedback"),
    path('get_feedback/', get_feedback_json, name='get_feedback_json'),
]