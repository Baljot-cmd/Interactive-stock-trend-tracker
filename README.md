## Interactive Stock Trend Tracker

An interactive, web‑based dashboard built with **Django 5** and **Chart.js** to visualize recent price history for stock tickers.  
You can view prices in a responsive line chart, see a tabular list of the latest points, and quickly switch between tickers.

### Features

- **JSON API** for price data: `/api/v1/price/<SYMBOL>/`
- **Interactive HTML view** with chart and table: `/api/v1/price/<SYMBOL>/view/`
- **Symbol dropdown** to switch between tickers (e.g. AAPL, GOOGL)
- **Auto‑refreshing chart** (every 10 seconds)
- **Mobile‑friendly UI** using Bootstrap 5

### Project structure

- `stock/` – Python virtual environment directory (not committed to GitHub)
  - `stockproject/` – Django project root  
    - `stockproject/` – core Django settings and URLs  
    - `stockapp/` – main app (models, views, URLs, templates)  
    - `db.sqlite3` – local SQLite database (ignored in git)

### Requirements

- Python 3.11+ (matches the venv you created)
- Django 5.x
- djangorestframework

If you are recreating the environment from scratch, install:

```bash
pip install django djangorestframework
```

### Running the project locally

1. **Activate your virtual environment** (if not already active):

   ```bash
   cd "D:\Interactive stock trend tracker\stock"
   Scripts\activate
   ```

2. **Run database migrations** (only needed the first time, or after model changes):

   ```bash
   cd stockproject
   python manage.py migrate
   ```

3. **(Optional) Load or create sample tickers and prices**  
   There are helper scripts you can use:

   ```bash
   python create_sample_tickers.py
   python check_endpoints.py
   ```

   Or you can create data via the Django shell / admin.

4. **Start the dev server**:

   ```bash
   python manage.py runserver
   ```

5. **Open the dashboard in your browser**:

   - Homepage (HTML): `http://127.0.0.1:8000/`  
   - Specific symbol (HTML): `http://127.0.0.1:8000/price/AAPL/view/`  
   - JSON API: `http://127.0.0.1:8000/api/v1/price/AAPL/`

### API overview

- **GET** `/api/v1/price/<SYMBOL>/`
  - Returns JSON:

    ```json
    {
      "symbol": "AAPL",
      "data": [
        { "time": "2025-11-26T22:23:53Z", "price": "175.50" },
        ...
      ]
    }
    ```

- **GET** `/price/<SYMBOL>/view/`
  - Renders `price_list.html` with:
    - Line chart of the most recent prices
    - Table of recent entries
    - Dropdown to switch tickers

### Notes

- The SQLite database (`db.sqlite3`) and virtualenv binaries are **ignored** by git and should not be pushed to GitHub.
- If you want to deploy this project, you will likely:
  - Move the venv out of the repo
  - Configure a proper database (PostgreSQL, etc.)
  - Set `DEBUG = False` and configure `ALLOWED_HOSTS` and static files.


