import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

def get_officer_information(organization_name):
    base_url = "https://www.stuorg.iastate.edu{}/officers".format(organization_name)
    prefix_to_match = "http://info.iastate.edu/individuals/search/"
    role_to_exclude = "Nope" 

    try:
        response = requests.get(base_url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, 'html.parser')

        specific_hyperlinks = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith(prefix_to_match)]

        officer_info = {}
        for link in specific_hyperlinks:
            role = soup.find('a', {'href': link}).find_previous('th').text.strip()
            if role.lower() != role_to_exclude.lower():
                officer_name = soup.find('a', {'href': link}).text.strip()
                officer_email = urlparse(link).path.split("/")[-1]
                officer_info[role] = {'name': officer_name, 'email': officer_email}

        return officer_info

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def save_to_json_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    organized_links_file_path = "organized_links.json"
    output_file_path = "officer_information.json"

    with open(organized_links_file_path, 'r', encoding='utf-8') as json_file:
        organized_links = json.load(json_file)

    all_officer_information = {}

    for organization_name, website_links in organized_links.items():
        organization_info = {}
        for subtext in website_links:
            officer_information = get_officer_information(subtext)
            if officer_information:
                organization_info[subtext] = officer_information
        all_officer_information[organization_name] = organization_info

    save_to_json_file(output_file_path, all_officer_information)

    print(f"Officer information saved to {output_file_path}.")
