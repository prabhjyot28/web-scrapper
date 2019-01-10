from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

url = "http://www.myneta.info/ls2014/index.php?action=show_winners&sort=default"
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")


filename = "loksabha_winners2014.csv"
f = open(filename, "w")
headers = "Candidate,Constituency,Party,Criminal Case(s),Education,Total Assets,Liabilities\n"
f.write(headers)


containers = page_soup.findAll("table")
body = containers[2].findAll('tr')
body.pop(0)
body.pop(0)


for leader in body:
    elements = leader.findAll('td')
    
    constituency = elements[2].text
    party = elements[3].text
    cases = elements[4].text
    education = elements[5].text
    assets = elements[6].text
    assets = assets.split('~')[0]
    assets = assets.replace(',', '')
    liability = elements[7].text
    liability = liability.split('~')[0]
    liability = liability.replace(',', '')
    name = elements[1].findAll('a')
    candidate = name[1].text
    candidate = candidate.replace(',','')

    f.write(candidate+","+constituency+","+party+","+cases+","+education+","+assets+","+liability+"\n")

f.close()   




