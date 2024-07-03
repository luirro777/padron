from django.core.management.base import BaseCommand, CommandError
from afiliados.models import Mesa
import csv
from django.db import transaction

class Command(BaseCommand):
    help = 'Importa datos desde un archivo CSV al modelo Mesa'

    def add_arguments(self, parser):
        parser.add_argument('mesas_csv', type=str, help='Archivo CSV de Mesas')

    @transaction.atomic
    def handle(self, *args, **options):
        mesas_csv = options['mesas_csv']
        
        try:
            with open(mesas_csv, 'rt') as csvfile_m:
                spamreader_m = csv.reader(csvfile_m, delimiter=',', quotechar='"')
                for row in spamreader_m:
                    num = row[0]
                    prov = row[1]
                    depa = row[2]
                    deno = row[3]
                    dire = row[4]
                    loca = row[5]
                    ubic = row[6] 
                    
                    Mesa.objects.update_or_create(
                        numero=num,
                        defaults={
                            'provincia': prov,
                            'departamento': depa,
                            'denominacion': deno,
                            'direccion': dire,
                            'localidad': loca,
                            'ubicacion_geografica': ubic
                        }
                    )
                self.stdout.write(self.style.SUCCESS('Importación de mesas finalizada'))

        except FileNotFoundError as e:
            raise CommandError(f'Archivo no encontrado: {e.filename}')
        except csv.Error as e:
            raise CommandError(f'Error leyendo archivo CSV: {e}')
        except Exception as e:
            raise CommandError(f'Error inesperado: {str(e)}')
