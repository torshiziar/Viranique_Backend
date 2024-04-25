from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from device.models import Sensor
from history.serializers import HistorySerializer
logger = logging.getLogger('django')

class HistoryView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)  # Owner
    serializer_class = HistorySerializer



    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        logger.debug(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
