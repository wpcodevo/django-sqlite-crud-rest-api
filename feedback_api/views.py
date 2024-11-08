from rest_framework.response import Response
from rest_framework import status, generics
from feedback_api.models import FeedbackModel
from feedback_api.serializers import FeedbackSerializer
import math
from datetime import datetime

class Feedback(generics.GenericAPIView):
    serializer_class = FeedbackSerializer
    queryset = FeedbackModel.objects.all()

    def get(self, request):
        page_num = int(request.GET.get("page", 1))
        limit_num = int(request.GET.get("limit", 10))
        start_num = (page_num - 1) * limit_num
        end_num = limit_num * page_num
        search_param = request.GET.get("search")
        feedback = FeedbackModel.objects.all()
        total_feedback = feedback.count()
        if search_param:
            feedback = feedback.filter(title__icontains=search_param)
        serializer = self.serializer_class(feedback[start_num:end_num], many=True)
        return Response({
            "status": "success",
            "total": total_feedback,
            "page": page_num,
            "last_page": math.ceil(total_feedback / limit_num),
            "feedbacks": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"feedback": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class FeedbackDetail(generics.GenericAPIView):
    queryset = FeedbackModel.objects.all()
    serializer_class = FeedbackSerializer

    def get_feedback(self, pk):
        try:
            return FeedbackModel.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        feedback = self.get_feedback(pk=pk)
        if feedback == None:
            return Response({"status": "fail", "message": f"Feedback with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(feedback)
        return Response({"status": "success", "data": {"feedback": serializer.data}})

    def patch(self, request, pk):
        feedback = self.get_feedback(pk)
        if feedback == None:
            return Response({"status": "fail", "message": f"Feedback with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            feedback, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(updatedAt=datetime.now())
            return Response({"status": "success", "data": {"feedback": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        feedback = self.get_feedback(pk)
        if feedback == None:
            return Response({"status": "fail", "message": f"Feedback with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
