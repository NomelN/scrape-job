# Pôle Emploi Job Scraper
![téléchargement](https://github.com/NomelN/scrape-job/assets/61651276/25c8f840-6434-4f93-8b75-6f0dbe8e219c)



This Python script is designed to scrape job postings from the Pôle Emploi website for a specific profession and location. It uses the `requests`, `beautifulsoup4`, and `pandas` libraries to fetch and process the job data.


## Prerequisites

Before using this script, ensure you have the following dependencies installed:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4 
```

## Getting Started
Clone this repository to your local machine:
```bash
git clone https://github.com/NomelN/scrape-job.git
```
Run the script to scrape job postings:
```bash
python scrape_jobs.py
```
## Usage
You can modify the script's parameters to target specific job searches by editing the current_page URL, profession, and location details.

in the URL of the `current_page`, modify the following elements to have the data specific to your search.

current_page = 'https://candidat.pole-emploi.fr/offres/recherche?lieux={your_location}&motsCles={your_job}&offresPartenaires=true&rayon=10&tri=0'

`{your_location}` replaced by your geographical area.

`{your_job}` replaced by the desired job

example: if you want to search for France, you must enter {01P}; P designates country and 01 France



## Methods
The script provides two methods for scraping job postings:

   ### First Method:

  Retrieves job page URLs.
  Extracts job details such as title, company, location, description, contract, and date.
  Saves data to an Excel file (jobs-pole_emploi.xlsx).

  ### Second Method:
  
  Retrieves job posting URLs.
  Extracts job details (all informations), including title, company, location, description, contract, date, and more.
  Saves data to an Excel file (jobs.xlsx).
  You can choose the method that suits your needs.

## Output
The scraped job data will be saved in an Excel file in the root directory of the project:

jobs-pole_emploi.xlsx (First Method)
jobs.xlsx (Second Method)
