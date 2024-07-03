from email.policy import default
from django.db import models

# Create your models here.

class Mesa(models.Model):
    """Model definition for Mesa."""

    numero = models.PositiveIntegerField("Numero de mesa",default=0)
    denominacion = models.CharField("Denominacion", max_length=80)
    direccion = models.CharField("Direccion", max_length=80)
    provincia = models.CharField("Provincia", max_length=80)
    departamento = models.CharField("Departamento", max_length=80)
    localidad = models.CharField("Localidad", max_length=80)
    ubicacion_geografica = models.CharField("Ubicación Geográfica", max_length=255, blank=True, null=True)

    class Meta:
        """Meta definition for Mesa."""

        verbose_name = 'Mesa'
        verbose_name_plural = 'Mesas'
    
   

    def __str__(self):
        """Unicode representation of Mesa."""
        return str(self.numero) + " - " + self.denominacion + " - " + self.direccion



class Afiliado(models.Model):
    """Model definition for MODELNAME."""

    apellidos = models.CharField("Apellidos", max_length=80)
    nombres= models.CharField("Nombres", max_length=80)    
    dni = models.CharField('DNI (sin puntos)', max_length=80)
    organizacion = models.CharField("Organizacion", max_length=80)    
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Afiliado'
        verbose_name_plural = 'Afiliados'    

    

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.apellidos + ", " + self.nombres + " - Mesa:" + str(self.mesa.numero)

