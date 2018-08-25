#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import cs

url = '#untitle website's URL'

count = 90000
with open('anime.csv', 'w', newline='') as anime:
    csvwriter = csv.writer(anime)
    while count <= 99999:
        url2 = url + str(count)
        print(url2)
        uh = urllib.request.urlopen(url2, [timeout=3])
        data = uh.text
        soup = BeautifulSoup(data, "html.parser")
        tags = soup.find('font')
        count += 1
        if tags is None:
            continue

        for tag in tags:
            csvwriter.writerow([tag, count])

