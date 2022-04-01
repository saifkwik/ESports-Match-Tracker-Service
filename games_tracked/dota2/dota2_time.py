from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
# from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(executable_path="chrome_driver/chromedriver.exe", options=options)
# browser = webdriver.Chrome(executable_path="/match-tracker/api_esports_matches/chrome_driver/chromedriver", 
# options=options) 

browser.get("https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches")
html_source = browser.page_source

browser.close()
soup = BeautifulSoup(html_source, 'html.parser')
divTag = soup.find_all("span", class_="match-countdown")

# pprint.pprint(divTag)
a = []
t = 0
for tag in divTag:
    v = tag.find_all("span", class_="timer-object-date")
    for teams in v:
        a.append(v[0].get_text().replace('\n', '').replace('\t', ''))

time_strings = a[0:15]
dota2_time = []
for time in time_strings:
    e = time.replace(' 2022 -', '').split()
    dota2_time.append(f'{e[2]}- {e[1]}{e[0]}'.replace(',', ' '))
