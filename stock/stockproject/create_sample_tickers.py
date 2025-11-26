import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockproject.settings')
django.setup()

from stockapp.models import Ticker

print('Creating sample tickers...')
Ticker.objects.update_or_create(symbol='AAPL', defaults={'name': 'Apple Inc.'})
Ticker.objects.update_or_create(symbol='GOOGL', defaults={'name': 'Alphabet Inc.'})
print('Sample tickers created.')
