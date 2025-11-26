from django.urls import path
from . import views

urlpatterns = [
    # Homepage: render price_list.html for a default symbol
    # Available at /
    path('', views.PriceDataHTMLView.as_view(), {'symbol': 'AAPL'}, name='home'),

    # JSON API: /api/v1/price/<symbol>/
    path('price/<str:symbol>/', views.PriceDataStandardView.as_view(), name='price-list'),

    # HTML view for browsers: /api/v1/price/<symbol>/view/
    path('price/<str:symbol>/view/', views.PriceDataHTMLView.as_view(), name='price-list-html'),
]