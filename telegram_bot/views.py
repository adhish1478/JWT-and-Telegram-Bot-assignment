# telegram_bot/views.py

import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import TelegramUser

@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        print("Webhook hit ✅")
        data = json.loads(request.body)

        message = data.get("message", {})
        if message.get("text") == "/start":
            user = message.get("from", {})
            telegram_id = user.get("id")
            username = user.get("username")
            first_name = user.get("first_name")
            last_name = user.get("last_name")

            TelegramUser.objects.update_or_create(
                telegram_id=telegram_id,
                defaults={
                    "username": username,
                    "first_name": first_name,
                    "last_name": last_name,
                }
            )

        return JsonResponse({"ok": True})
    return JsonResponse({"error": "Invalid request"}, status=400)
    