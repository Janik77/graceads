from django.db import models


class PartnerLogo(models.Model):
    name = models.CharField(max_length=120, blank=True)
    logo = models.ImageField(upload_to="partner_logos/")
    is_active = models.BooleanField(default=True)
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.name or f"Partner {self.id}"
