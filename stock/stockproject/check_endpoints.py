import urllib.request

URLS = [
    'http://127.0.0.1:8000/api/v1/price/AAPL/',
    'http://127.0.0.1:8000/api/v1/price/AAPL/view/'
]

for url in URLS:
    print('\nREQUEST ->', url)
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            status = r.getcode()
            body = r.read()
            print('Status:', status)
            print('Body (first 1000 chars):\n')
            try:
                print(body.decode('utf-8')[:1000])
            except Exception:
                print(body[:1000])
    except Exception as e:
        print('ERROR:', repr(e))
