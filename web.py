import requests
from bs4 import BeautifulSoup
import csv


page = requests.get("https://witanime.quest/%d9%85%d9%88%d8%a7%d8%b9%d9%8a%d8%af-%d8%a7%d9%84%d8%ad%d9%84%d9%82%d8%a7%d8%aa/")

src = page.content
soup = BeautifulSoup(src, "lxml")

contents = soup.find_all("div",{"class":"main-widget"})

number_of_days = len(contents)
n = []
for i in range (number_of_days):
    days = contents[i].find('h3').text.strip()
    All_anime = contents[i].find_all("div",{"class":"col-lg-2 col-md-4 col-sm-6 col-xs-6 col-no-padding col-mobile-no-padding"})
    number_of_anime = len(All_anime)

    for j in range(number_of_anime):
        names_of_anime = All_anime[j].find('h3').text.strip()
        n.append({"اليوم":days , "الانمي" : names_of_anime})


keys = n[0].keys()

with open("C:\\Users\\20100\\Documents\\PythonProjects\\Web_Scraping\\animeEp.csv","w") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader(keys)
        dict_writer.writerows(n)
        print("file is created")

