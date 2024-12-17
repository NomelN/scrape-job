#Import of modules

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

"""We choose like:
profession: IT (informatique) and workplace: France (01P)"""

base_url = 'https://candidat.francetravail.fr/'
current_page = 'https://candidat.francetravail.fr/offres/recherche?lieux=01P&motsCles=informatique&offresPartenaires=true&rayon=10&tri=0'
pages = []

print("Retrieving page URLs...")

def get_pages(current_page):
    response = requests.get(current_page)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'id': 'zoneAfficherPlus'})
        if div:
            next_page_link = div.find('a')
            if next_page_link:
                next_page_url = urljoin(base_url, next_page_link.get('href'))
                pages.append(next_page_url)
                return next_page_url
        else:
            return None  # No more next pages
    else:
        print(f"Failed to fetch {page_url}. Status code: {response.status_code}")
        return None

while True:
    pages.append(current_page)
    html_doc = requests.get(current_page).text
    soup = BeautifulSoup(html_doc, "html.parser")
    current_page = get_pages(current_page)
    if current_page is None:
        break
print("End page URL recovery.")

print("start of sorting the list of pages...")
pages_list = []
for i in pages:
    if i not in pages_list:
        pages_list.append(i)
print("end of sorting the list of pages.")

#Get content of offers
offer = []
print("start of information extraction...")
def get_offer(page):
    html_doc = requests.get(page).text
    soup = BeautifulSoup(html_doc, 'html.parser')
    lis = soup.find_all('li', class_='result')

    for li in lis:
        try:
            title = li.find('h2', class_='t4 media-heading').text.strip()
        except:
            title = ''
        
        try:
            job_link = li.find('a', class_='media with-fav').get('href')
            job_link = urljoin(base_url, job_link)
        except:
            job_link = ''
        
        try:
            company = li.find('div', class_='media-body').find('p', class_='subtext').text.split('-')
            company = company[0].strip()
        except:
            company = ''
        
        try:
            localisation = li.find('div', class_='media-body').find('p', class_='subtext').find('span').text.strip()
        except:
            localisation = ''
        
        try:
            description = li.find('div', class_='media-body').find('p', class_='description').text.strip()
        except:
            description = ''
        
        try:
            contract = li.find('div', class_='media-body').find('p', class_='contrat visible-xs').text.split('-')
            contract = contract[0].strip() + ' - ' + contract[1].strip()
        except:
            contract = ''

        try:
            date = li.find('div', class_='media-body').find('p', class_='date').text.strip()
        except:
            date = ''

        job = {
            'Title': title,
            'Company': company,
            'Localisation': localisation,
            'Description': description,
            'Contract': contract,
            'Date': date,
            'Job_link': job_link,
            }
        offer.append(job)

for page in pages_list:
    get_offer(page)
print("start of information extraction.")

#Save the data to a excel file
print("start of saving in csv file...")
df = pd.DataFrame(offer)
df.to_csv("jobs-pole_emploi.csv")
print("End of saving in csv file.")