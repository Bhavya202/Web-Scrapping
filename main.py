# Importing Modules
import requests
from bs4 import BeautifulSoup
import csv

# Strarting URL and extracting Table from it
URL = requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars")
soup = BeautifulSoup(URL.text, "html.parser")

# Extracting headers from the table
headers_tag = soup.find_all("th")
headers = [headers.text.strip() for headers in headers_tag]

# Extracting rows from table
rows = []
data_rows = soup.find_all("tr")

# Adding data to the rows of the table
for row in data_rows:
    value = row.find_all("td")
    beautified_value = [ds.text.strip() for ds in value]
    
    if len(beautified_value) == 0:
        continue

    rows.append(beautified_value)

# Creating a csv file for the table
with open("data.csv", "w", encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)