from bs4 import BeautifulSoup
import requests
import re   
import html5lib

contagem=1

response = requests.get("https://en.wikipedia.org/wiki/Cybersecurity_information_technology_list")

tags = BeautifulSoup(response.text, "html5lib")

# Pega o tiulo da pag principal
title = tags.find("title")

# Pega todos os subititles da pag
subtitles = tags.find_all("h2")
[h2.text for h2 in subtitles]

# Pega todos os sites da pag
referencia = tags.find_all("p")

for table in referencia:
    links = table.find_all("a", href=re.compile("/wiki/"))
    for link in links:
        branch_file = link.get("title")
        print(f'Página secundária: {contagem} : {branch_file}')
        contagem+=1


print("Página princpal: ", title)
# print(subtitles)