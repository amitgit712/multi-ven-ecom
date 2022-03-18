from django.db import models
from django.utils.translation import gettext as _

from user.models import User


class Vendor(models.Model):
    name = models.CharField(max_length=250, null=True)
    created_by = models.OneToOneField(
        User, related_name='vendor',
        on_delete=models.CASCADE,
        verbose_name=_('Create by')
    )
    shop_name = models.CharField(
        verbose_name=_("shop name"), blank=False,
        null=True, max_length=250
    )
    description = models.TextField(verbose_name=_('description'), null=True)
    phone_number = models.CharField(
        verbose_name=_('phone number'), blank=False,
        null=False, max_length=11, default=0
    )

    is_account_closed = models.BooleanField(default=False)
    is_suspended = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return f' {self.shop_name} - Created by : {self.created_by.username}'
