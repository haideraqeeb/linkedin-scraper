from bs4 import BeautifulSoup
import requests

keywords = "Machine Learning"
location = "Bangalore"

link_url = f"https://www.linkedin.com/jobs/search?keywords={keywords}&location={location}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

response = requests.get(link_url)

list_page = response.text
soup = BeautifulSoup(list_page, "html.parser")
page_jobs = soup.find_all("li")
id_list = []

for job in page_jobs:
    base_card_div = job.find("div", {"class": "base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card"})
    if base_card_div != None:
        id = base_card_div.get("data-entity-urn").split(":")[3]
        id_list.append(id)

print(id_list)
