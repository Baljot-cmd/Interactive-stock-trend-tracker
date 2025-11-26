import importlib, traceback

try:
    m = importlib.import_module('stockapp.management.commands.fetch_prices')
    print('Imported module:', m)
    print('Has Command attribute?', hasattr(m, 'Command'))
    if hasattr(m, 'Command'):
        print('Command:', m.Command)
    else:
        print('Module dir:', [name for name in dir(m) if not name.startswith('_')])
except Exception:
    traceback.print_exc()
