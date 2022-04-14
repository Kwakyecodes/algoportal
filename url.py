# Import libraries
import requests
import re
from bs4 import BeautifulSoup

def get_data(url: str) -> str:
    '''Make request to fetch complete hmtl article and return it''' 
    r = requests.get(url)
    return r.text

def get_link(query: str) -> str:
    '''Get link to Geeks for Geeks code for query and return it'''
    query = query.replace(" ", "+")
    google = "https://www.google.com/search?q=geeks+for+geeks+" + query
    html = get_data(url=google)
    
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all("a")

    pattern = 'https://www.geeksforgeeks.org/[0-z,-]+/'
    for link in links:
        result = re.findall(pattern, f"{link}")
        if result:
            break
    if result:
        return result[0]
    else:
        return ''
