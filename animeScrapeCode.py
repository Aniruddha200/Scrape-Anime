from bs4 import BeautifulSoup
import requests
import csv
import lxml

url = '#untitle website's URL'

count = 90000
with open('anime.csv', 'w', newline='') as anime:
    csvwriter = csv.writer(anime)
    while count <= 99999:
        url2 = url + str(count)
        print(url2)
        uh = requests.get(url2, timeout=3)
        data = uh.text
        soup = BeautifulSoup(data, "lxml")
        tags = soup.find('font')
        count += 1
        if tags is None:
            continue

        for tag in tags:
            csvwriter.writerow([tag, count])

