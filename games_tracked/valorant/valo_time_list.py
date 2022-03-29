import requests
from bs4 import BeautifulSoup

url = 'https://vlr.gg'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# To get time of matches:
divTag = soup.find_all('div', class_='h-match-team')

time_list = []

# To get number of FINAL Matches:
final = []
for tag in divTag:
    v = tag.find_all("div", class_="h-match-eta mod-final")
    if v != []:
        final.append(v)
for final_matches in range(len(final)):
    time_list.append('FINAL')

# To get number of LIVE Matches
live = []
for tag in divTag:
    v = tag.find_all("div", class_="h-match-eta mod-live")
    if v != []:
        live.append(v)
# print(len(live))
for live_matches in range(len(live)):
    time_list.append('LIVE')

# To get timing of UPCOMING Matches:
upcoming = []
for tag in divTag:
    v = tag.find_all('div', class_='h-match-eta mod-upcoming')
    for time in v:
        upcoming.append(v[0].get_text().replace('\n', '').replace('\t', ''))

time_list = time_list + upcoming

# To make the list of time_list 15:
for times in time_list:
    if len(time_list) < 15:
        time_list.append(time_list[len(time_list) - 1])
time_strings = time_list[0:15]

t = 1
final_time_list = [time_strings[i:i + t] for i in range(0, len(time_strings), t)]
