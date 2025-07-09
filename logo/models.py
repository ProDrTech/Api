from django.db import models
from cloudinary.models import CloudinaryField
class SiteSettings(models.Model):
    logo = CloudinaryField("logo", blank=True, null=True)

    def __str__(self):
        return "Sayt Sozlamalari"  # ✅ doimiy string

    class Meta:
        verbose_name = "Sayt logosi"
        verbose_name_plural = "Sayt logosi"