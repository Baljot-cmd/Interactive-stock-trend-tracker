import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
django.setup()

from stockapp.models import PriceData

qs = PriceData.objects.select_related('ticker').order_by('-timestamp')[:50]
for p in qs:
    print(p.ticker.symbol, p.price, p.timestamp.isoformat())

print('Total PriceData rows:', PriceData.objects.count())
