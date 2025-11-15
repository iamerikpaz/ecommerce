# filepath: /home/erikpaz/medisunshine/ecommerce/context_processors.py
from django.conf import settings

def paypal_credentials(request):
    return {
        'PAYPAL_CLIENT_ID': settings.PAYPAL_CLIENT_ID,
    }