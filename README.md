# buyerScrap

Grocery budget planner. It scrapes current product prices from an online supermarket
(Condis) with Selenium and builds a shopping list that fits the budget you give it.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)

> Early prototype. Right now it scrapes a single category and fills the list greedily
> until the budget runs out.

## How it works

1. `scraping/market_scraper.py` opens the store in headless Chrome and reads product
   names and prices.
2. `logic/planificador.py` parses the prices and picks products until the budget is
   reached.
3. `gui/interfaz.py` is a small Tkinter window where you enter the budget and see the
   resulting list.

## Running it

Requires Python 3 and Chrome + chromedriver (update the driver path in
`scraping/market_scraper.py` if yours is somewhere else).

```bash
pip install -r requirements.txt
python main.py
```

## Next steps

- Scrape more categories and wire up the protein / dairy / vegetable filters
  (`logic/filtros.py`)
- Replace the fixed sleep with explicit Selenium waits
- Pick products by value (price per kg, nutrition) instead of first come first served
- Weekly and monthly plans
