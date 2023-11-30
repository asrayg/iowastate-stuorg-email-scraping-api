import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def get_last_parts_of_hyperlinks(url, startswith):
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        specific_hyperlinks = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith(startswith)]

        last_parts = [urlparse(link).path.split("/")[-1] for link in specific_hyperlinks]

        return last_parts

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    url = "https://www.stuorg.iastate.edu/stugov/officers"
    prefix_to_match = "http://info.iastate.edu/individuals/search/"
    
    last_parts = get_last_parts_of_hyperlinks(url, prefix_to_match)

    if last_parts:
        for part in last_parts:
            print(part)
    else:
        print(f"No hyperlinks starting with '{prefix_to_match}' found.")