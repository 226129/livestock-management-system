from django.db import models

# Create your models here.


class Livestock(models.Model):
    class Meta:
        ordering = ['earring_id']
        verbose_name_plural = 'Livestock'

    BREEDS = (
        ('Brangus', 'Brangus'),
        ('Cebu', 'Cebu'),
        ('Charbray', 'Charbray'),
        ('Charolais', 'Charolais'),
        ('Criollo', 'Criollo'),
    )

    SEXES = (
        ('Hembra', 'Hembra'),
        ('Macho', 'Macho'),
    )

    COLORS = (
        ('Barosa', 'Barosa'),
        ('Vayado', 'Vayado'),
        ('Café', 'Café'),
        ('Cara Blanca', 'Cara Blanca'),
        ('Colorado', 'Colorado'),
        ('Crullo', 'Crullo'),
        ('Melado', 'Melado'),
        ('Negro', 'Negro'),
        ('Pinto Decolorado', 'Pinto Decolorado'),
        ('Pinto de Negro', 'Pinto de Negro'),
        ('Sabina', 'Sabina'),
    )

    PURITY = (
        ("Si", "Si"),
        ("No", "No")
    )

    earring_id = models.IntegerField(
        primary_key=True, unique=True, help_text="Numero de arete")
    name = models.CharField(max_length=255, unique=True,
                            help_text="Nombre de la vaca")
    breed = models.CharField(
        max_length=255, choices=BREEDS, help_text="Raza de la vaca")
    sex = models.CharField(max_length=255, choices=SEXES,
                           help_text="Sexo de la vaca")
    register_date = models.DateField(help_text="Fecha de registro")
    color = models.CharField(
        max_length=255, choices=COLORS, help_text="Color de la vaca")
    cost = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Costo de la vaca al comprarla")
    birthdate = models.DateField(help_text="Fecha de nacimiento de la vaca")
    birthdate_weight = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Pesaje al momento de nacer")
    weaning = models.DateField(help_text="Fecha de destete de la vaca")
    weaning_weight = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Pesaje al momento del destete")
    grandfather = models.OneToOneField('self', on_delete=models.SET_NULL, null=True,
                                       blank=True, related_name='offspring_grandfather', help_text="Abuelo de la vaca")
    father = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='offspring_father', help_text="Padre de la vaca")
    mother = models.OneToOneField(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='offspring_mother', help_text="Madre de la vaca")
    photo = models.ImageField(upload_to='livestock_photos/', null=True, blank=True,
                              help_text="Foto de la vaca")
    origin = models.CharField(max_length=255, help_text="Origen de la vaca")
    purity = models.CharField(
        max_length=255, help_text="Pura de la vaca", choices=PURITY)

    def __str__(self):
        return f"{self.earing_id}: {self.name} ({self.breed})"


class LivestockWeight(models.Model):
    class Meta:
        ordering = ['date']
        verbose_name_plural = 'Livestock Weights'

    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, help_text="Vaca a la que se le pesó")
    name = models.CharField(max_length=255, unique=True,
                            help_text="Nombre de la vaca")
    breed = models.CharField(
        max_length=255, help_text="Raza de la vaca")
    date = models.DateField(help_text="Fecha del pesaje")
    weight = models.FloatField(help_text="Peso de la vaca")
    photo = models.ImageField(null=True, blank=True,
                              help_text="Foto de la vaca")

    def save(self, *args, **kwargs):
        self.name = self.livestock.name
        self.breed = self.livestock.breed
        self.photo = self.livestock.photo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.livestock.earring_id}: {self.weight}kg on {self.date}"


class LivestockDeparture(models.Model):
    class Meta:
        ordering = ['date']
        verbose_name_plural = "Livestock Departures"

    DEPARTURE_TYPES = (
        ('Venta', 'Venta'),
        ('Muerte', 'Muerte'),
        ('Regalo', 'Regalo'),
    )

    livestock = models.ForeignKey(
        Livestock, on_delete=models.CASCADE, help_text="Vaca que se fue")
    name = models.CharField(max_length=255, unique=True,
                            help_text="Nombre de la vaca")
    breed = models.CharField(max_length=255, help_text="Raza de la vaca")
    departure_reason = models.CharField(
        max_length=20, choices=DEPARTURE_TYPES, help_text="Motivo de la salida")
    date = models.DateField(help_text="Fecha de la salida")
    price = models.FloatField(
        help_text="Precio de la vaca", null=True, blank=True)
    photo = models.ImageField(null=True, blank=True,
                              help_text="Foto de la vaca")
    notes = models.CharField(max_length=255, help_text="Notas adicionales")

    def save(self, *args, **kwargs):
        self.name = self.livestock.livestock_name
        self.breed = self.livestock.breed
        self.photo = self.livestock.photo
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.livestock.earring_id}: {self.departure_reason} on {self.date}"
