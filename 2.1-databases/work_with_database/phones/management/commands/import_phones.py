import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            phone_id = int(phone['id'])
            name = phone['name']
            image = phone['image']
            price = float(phone['price'])
            release_data =phone['release_date']
            lte_exists = phone['lte_exists'].lower() in ('true', '1')
            
            Phone.objects.update_or_create(
                id= phone_id,
                defaults={
                    'name': name,
                    'image': image,
                    'price': price,
                    'release_date': release_data,
                    'lte_exists': lte_exists
                    }
                )
        self.stdout.write(self.style.SUCCESS('✅ Данные успешно импортированы'))