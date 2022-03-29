from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

browser = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe", options=options)

browser.get("https://ggscore.com/en/csgo/matches")
html_source = browser.page_source
browser.close()

soup = BeautifulSoup(html_source, 'html.parser')

divTag = soup.find_all('div', class_='mlist col-md-8')

n = []
m = 0
for tag in divTag:
    v = tag.find_all("td", class_="tdate")
    for teams in v:
        n.append(v[m].get_text().replace('\n', '').replace('\t', ''))
        m += 1

time_strings = n[0:15]

q = 0
for time in time_strings:
    if time == '':
        time_strings[q] = time.replace('', 'LIVE')
        q += 1

z = 1
time_list = [time_strings[i:i + z] for i in range(0, len(time_strings), z)]
