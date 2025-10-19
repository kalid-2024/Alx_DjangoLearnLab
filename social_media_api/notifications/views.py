from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.notifications.all()
        serialized = [
            {
                "actor": n.actor.username,
                "verb": n.verb,
                "target": str(n.target) if n.target else None,
                "read": n.read,
                "timestamp": n.timestamp
            }
            for n in notifications
        ]
        return Response(serialized)
