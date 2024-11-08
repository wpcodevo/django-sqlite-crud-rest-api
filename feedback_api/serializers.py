from rest_framework import serializers
from feedback_api.models import FeedbackModel


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackModel
        fields = '__all__'
