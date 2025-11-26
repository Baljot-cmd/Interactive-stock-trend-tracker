from django.shortcuts import render
from django.utils import timezone
from .models import Ticker, PriceData
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.

class PriceDataStandardView(ListView):
    model = PriceData

    def get_queryset(self):
        symbol = self.kwargs['symbol'].upper()
        ticker_instance = get_object_or_404(Ticker,symbol=symbol)
        return PriceData.objects.filter(ticker=ticker_instance).order_by('-timestamp')[:50]
    
    def render_to_response(self, context, **response_kwargs):
        # Use the queryset that Django provides in the context (object_list)
        # or fall back to calling get_queryset().
        data = context.get('object_list', self.get_queryset())
        formatted_data = [
            {'time': p.timestamp.isoformat(), 'price': str(p.price)}
            for p in data
        ]

        response_data = {
            'symbol': self.kwargs['symbol'].upper(),
            'data': formatted_data,
        }

        return JsonResponse(response_data)


class PriceDataHTMLView(PriceDataStandardView):
    """Render the same queryset as HTML using a template."""
    template_name = 'stockapp/price_list.html'

    def render_to_response(self, context, **response_kwargs):
        # Let Django render the template with the context provided by ListView
        return render(self.request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Provide the symbol and a timestamp for the template
        context['symbol'] = self.kwargs.get('symbol', '').upper()
        # Provide the list of available tickers for the dropdown
        context['tickers'] = Ticker.objects.all().order_by('symbol')
        context['now'] = timezone.now()
        return context