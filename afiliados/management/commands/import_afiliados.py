from django.core.management.base import BaseCommand, CommandError
from afiliados.models import Afiliado, Mesa
import csv
from django.db import transaction

class Command(BaseCommand):
    help = 'Importa datos desde un archivo CSV al modelo Afiliado'

    def add_arguments(self, parser):
        parser.add_argument('padron_csv', type=str, help='Archivo CSV de Padron')

    @transaction.atomic
    def handle(self, *args, **options):
        padron_csv = options['padron_csv']
        
        try:
            with open(padron_csv, 'rt') as csvfile_p:
                spamreader_p = csv.reader(csvfile_p, delimiter=',', quotechar='"')
                for row in spamreader_p:
                    docu = row[0]
                    ape = row[1]
                    nom = row[2]
                    orga = row[3]
                    nro_mesa = row[4]
                    
                    try:
                        mesa = Mesa.objects.get(numero=nro_mesa)
                    except Mesa.DoesNotExist:
                        self.stdout.write(self.style.WARNING(f'Mesa con número {nro_mesa} no existe'))
                        continue
                    
                    Afiliado.objects.update_or_create(
                        dni=docu,
                        defaults={
                            'apellidos': ape,
                            'nombres': nom,
                            'organizacion': orga,
                            'mesa': mesa
                        }
                    )
                self.stdout.write(self.style.SUCCESS('Importación de padrones finalizada'))

        except FileNotFoundError as e:
            raise CommandError(f'Archivo no encontrado: {e.filename}')
        except csv.Error as e:
            raise CommandError(f'Error leyendo archivo CSV: {e}')
        except Exception as e:
            raise CommandError(f'Error inesperado: {str(e)}')
