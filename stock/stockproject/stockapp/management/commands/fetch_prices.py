import requests
import time
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.db import transaction
from ...models import Ticker, PriceData

API_KEY = "404KCP5WL7GFOEO8"
BASE_URL = "https://www.alphavantage.co/query?"

class Command(BaseCommand):
    help = 'fetch the latest price data for all tracked tickers from a remote API'
    def handle(self, *args, **options):
        # Start process
        self.stdout.write("Starting price data fetch process...")

        tickers = Ticker.objects.all()
        if not tickers:
            self.stdout.write(self.style.WARNING("No tickers found in database. Aborting."))
            return

        for ticker in tickers:
            self.stdout.write(f"-> fetching data for {ticker.symbol}...")

            try:
                # Placeholder: replace with real API call using requests
                if ticker.symbol == 'AAPL':
                    raw_price_str = "175.50"
                elif ticker.symbol == 'GOOGL':
                    raw_price_str = "1500.75"
                else:
                    raw_price_str = "0.00"

                if not raw_price_str:
                    self.stdout.write(self.style.ERROR(f"API returned no price data for {ticker.symbol}."))
                    continue

                # Convert and persist
                price_decimal = Decimal(raw_price_str)
                with transaction.atomic():
                    PriceData.objects.create(
                        ticker=ticker,
                        price=price_decimal,
                    )
                self.stdout.write(self.style.SUCCESS(
                    f"Successfully recorded price for {ticker.symbol}: ${price_decimal}"
                ))

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.ERROR(f"Connection Error for {ticker.symbol}: {e}"))
                # brief backoff
                time.sleep(0.5)

            except (ValueError, Decimal.InvalidOperation) as e:
                self.stdout.write(self.style.ERROR(f"Data Conversion Error for {ticker.symbol}: {e}"))
                time.sleep(0.5)

        self.stdout.write("Price data fetch process finished.")