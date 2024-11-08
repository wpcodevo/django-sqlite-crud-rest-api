from django.urls import path
from feedback_api.views import Feedback, FeedbackDetail

urlpatterns = [
    path('', Feedback.as_view()),
    path('<str:pk>', FeedbackDetail.as_view())
]
