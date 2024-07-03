from django.db import models

from django.db.models import Q

class AfiliadoManager(models.Manager):


    def resultado(self, nro_legajo, nro_dni):
        lugar_votacion = self.filter(
            legajo = nro_legajo,
            dni = nro_dni
        )