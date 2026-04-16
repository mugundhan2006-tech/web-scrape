# Web Scraper for Top Headline

This script scrapes the top headline from a news website (defaults to BBC News).

## Usage

Run the script using Python:

```bash
python scrape.py
```

## Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

## Customization

To scrape from a different news website, modify the `url` parameter in the `get_top_headline()` function call.

## Troubleshooting

- If the script fails to find the headline, the website's HTML structure may have changed. Inspect the page source and update the selector in the code.
- Ensure you have an active internet connection.
- If blocked by the website, consider using headers or proxies (not implemented here).