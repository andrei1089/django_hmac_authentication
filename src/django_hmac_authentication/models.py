# Create your models here.
import uuid

from django.conf import settings
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext_lazy as _

user_model = settings.AUTH_USER_MODEL


class ApiHMACKey(models.Model):
    created_at = DateTimeField(auto_now_add=True, db_index=True)
    modified_on = DateTimeField(auto_now=True, db_index=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        user_model, on_delete=models.CASCADE, related_name='api_secrets'
    )
    secret = models.CharField(_('Secret'), max_length=512, null=False, editable=False)
    salt = models.CharField(_('Salt'), max_length=80, null=False, editable=False)
    revoked = models.BooleanField(_('Revoked'), default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'API Secret'
        verbose_name_plural = 'API Secrets'
