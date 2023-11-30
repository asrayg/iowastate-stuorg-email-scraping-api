import requests
from bs4 import BeautifulSoup
import json

def extract_links_from_website(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            if href.startswith('/') and href not in ('/', '/student-engagement', '/organizations', '/help') and \
                    '.edu' not in href and '.com' not in href and href.count('/') < 2:
                links.append(href)
        
        return links
    elif response.status_code == 404:
        print(f"Page not found. Status code: {response.status_code}")
        return None
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
        return None

def organize_links_by_website(base_url, exclude_numbers):
    all_links = {}  

    for i in range(1, 31):
        if i not in exclude_numbers:
            url = base_url.format(i)
            website_links = extract_links_from_website(url)
            
            if website_links:
                all_links[url] = website_links

    return all_links

if __name__ == "__main__":
    base_url = "https://www.stuorg.iastate.edu/organizations/{}/type"
    exclude_numbers = {7, 18, 26}

    organized_links = organize_links_by_website(base_url, exclude_numbers)

    with open('organized_links.json', 'w', encoding='utf-8') as json_file:
        json.dump(organized_links, json_file, indent=2)

    print("Organized links written to organized_links.json")
