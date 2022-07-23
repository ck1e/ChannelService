from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Order, ChannelNotification
from .apps import up_orders


@csrf_exempt
def core(request):
    # If there were changes in the Google Sheets.
    if 'X-Goog-Resource-State' in request.headers and request.headers['X-Goog-Resource-State'] == 'update' \
            and 'X-Goog-Changed' in request.headers and 'content' in request.headers['X-Goog-Changed']:
        print(request.headers)
        up_orders()

    return HttpResponse(f"")
