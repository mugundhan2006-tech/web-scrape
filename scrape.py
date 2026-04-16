import requests
from bs4 import BeautifulSoup

def get_top_headline(url='https://www.bbc.com/news'):
    """
    Scrape the top headline from the given news website URL.
    Defaults to BBC News.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the top headline - assuming it's the first article link
        headline_tag = soup.find('a', href=lambda x: x and '/news/articles/' in x)
        if headline_tag:
            headline = headline_tag.text.strip()
            return headline
        else:
            # Fallback: find the first h3
            headline_tag = soup.find('h3')
            if headline_tag:
                return headline_tag.text.strip()
            else:
                return "Top headline not found."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    headline = get_top_headline()
    print("Top Headline:", headline)