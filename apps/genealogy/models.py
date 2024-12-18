from django.db import models
from livestock.models import Livestock, LivestockDeparture, LivestockWeight

# Create your models here.


class LivestockPregnancies(models.Model):
    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Livestock Pregnancies'

    livestock = models.ForeignKey(
        Livestock, on_delete=models.PROTECT, help_text="Vaca preñada")
    diagnostic_date = models.DateField(help_text="Fecha de preñez")
    expected_due_date = models.DateField(
        help_text="Fecha probable de parto", null=True, blank=True)
    observations = models.CharField(max_length=255, help_text="Observaciones")
    weeks_pregnant = models.PositiveIntegerField(null=True, blank=True)
