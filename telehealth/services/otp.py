from django.conf import settings
import requests


def send_sms(phone, message):

    if settings.DEBUG:
        return {
            "status": True,
        }

    payload = {
        'AppSid': '',
        'SenderID': '',
        'Recipient': phone,
        'Body': message
    }

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post('url', data=payload, headers=headers)

    if response.json()["success"] == "true":
        return {
            "status": True,
            "message": str(response.json())
        }
    else:
        return {
            "status": False,
            "message": str(response.json())
        }
