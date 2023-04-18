from django.utils.functional import SimpleLazyObject, lazy

from .models import Message


def inbox(request):
    if request.user.is_authenticated:
        return {'messenger_unread_count': lazy(
            lambda: Message.objects.filter(
            recipient=request.user,
            read_at__isnull=True,
            recipient_deleted_at__isnull=True).count(),
            int
        )}
    else:
        return {}
