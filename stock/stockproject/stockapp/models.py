from django.db import models

# Create your models here.

class Ticker(models.Model):
    symbol = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.symbol
    
class PriceData(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE, related_name='price')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    timestamp = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        ordering = ['-timestamp']