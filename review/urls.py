from django.urls import path
from . import views
urlpatterns = [
    path('<str:slug>', views.WriteReview, name='write_review'),
]
