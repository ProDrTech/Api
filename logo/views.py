from rest_framework.views import APIView
from rest_framework.response import Response
from logo.models import SiteSettings
from logo.serializers import SiteSettingsSerializer

class SiteSettingsView(APIView):
    def get(self, request):
        obj = SiteSettings.objects.last()
        serializer = SiteSettingsSerializer(obj)
        return Response(serializer.data)
