from django.conf import settings
from django.db import models
from django.utils.timezone import now
from datetime import timedelta


class MessageManager(models.Manager):
    def get_queryset(self):
        max = now() - timedelta(days=365)
        return super().get_quryset().filter(sent_at_gte=max)


# Create your models here.
class Message(models.Model):
    subject = models.CharField("sujet", max_length=120)
    body = models.TextField("corps", blank=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               related_name='sent_messages',
                               verbose_name="expéditeur")
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='received_messages',
        verbose_name="destinataire")
    sent_at = models.DateTimeField(
        "envoyé le", default=now)

    objects = models.Manager()
    recent_object = MessageManager()

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"
        ordering = ['-sent_at', '-id']
