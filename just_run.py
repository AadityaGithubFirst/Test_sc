from bs4 import BeautifulSoup
import requests
from time import sleep
URL = "https://flag.dol.gov/processingtimes"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
old_job_elements = soup.find("td", class_="xl71").text
old_job_element = soup.find("td", class_="xl72").text
old_job_elemen = soup.find_all("td", class_="xl72")[1].text
while True:
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find("td", class_="xl71").text
    job_element = soup.find("td", class_="xl72").text
    job_elemen = soup.find_all("td", class_="xl72")[1].text
    if (old_job_elements==job_elements) and (old_job_element==job_element) and (old_job_elemen==job_elemen):
        print(f"They have not changed")
        sleep(3600*24)
    else:
        print("Look at https://flag.dol.gov/processingtimes the values of changed the website should be looked at.")
        print(f"They are now Analyst Review = {job_elements}, Audit Review = {job_element}, Reconsideration Request to the CO = {job_elemen}")
        break    