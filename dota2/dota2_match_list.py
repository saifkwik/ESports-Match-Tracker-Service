import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime
from dota2 import dota2_time

url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

divTag = soup.find_all('div', class_='scroll-logged-out')

a = []
x = 0
for tag in divTag:
    v = tag.find_all("span", class_="team-template-text")
    for teams in v:
        a.append(v[x].get_text().replace('\n', '').replace('\t', ''))
        x += 1

team_strings = a[0:30]

t = 1
team_list = [team_strings[i:i + t] for i in range(0, len(team_strings), t)]

final_team_list = []
y = 0
for final in range(30):
    try:
        final_team_list.append(team_list[y] + team_list[y + 1])
        y += 2
    except IndexError as i:
        pass
# pprint.pprint(final_team_list)
# print(len(final_team_list))

# import database from sql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rango6",
    database='game_database'
)

mycursor = mydb.cursor()

# Inserting Match detail to table:
o = 1
u = 0
dota2_team_list = []  # Creating team list for API
for values in range(15):
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    # sql_insert = 'INSERT INTO DOTA2_MATCHES (_INDEX, TEAMS, TIME_IST, Last_updated) VALUES(%s, %s, %s, %s)'
    sql_insert = 'UPDATE DOTA2_MATCHES SET TEAMS = %s, TIME_IST = %s, Last_updated = %s WHERE _INDEX = %s'
    val = (
        str(f'{final_team_list[u][0]} VS {final_team_list[u][1]}'), str(dota2_time.dota2_time[u]), str(current_time), str(o))
    e = str(f'{final_team_list[u][0]} VS {final_team_list[u][1]}')
    dota2_team_list.append(e)
    mycursor.execute(sql_insert, val)
    mydb.commit()
    o += 1
    u += 1


# Merging Match names with time of Matches and converting it in a dictionary
dota2_dict = dict(zip(dota2_team_list, dota2_time.dota2_time))
print(f'DOTA2 Matches Schedule Updated successfully!')