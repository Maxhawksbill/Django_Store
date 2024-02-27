from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from .client import send_message


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def telegram(request):
    # Telegram webhook view
    # Get telegram message
    # Echo message
    print(request.data)

    text = request.data['message']['text']
    name = request.data['message']['from'].get('first_name')

    telegram_text = f"{name}: {text}"

    send_message(912697577, telegram_text)

    # Some comment

    return Response({'status': 'OK!'})

