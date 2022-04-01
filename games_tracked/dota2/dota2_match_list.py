import requests
from bs4 import BeautifulSoup
from datetime import datetime
from games_tracked.dota2 import dota2_time
from db import database


# from dateutil.tz import gettz
# from utils.logs_handler import create_logger

# logger = create_logger(__name__, remote_logging=False)

def dota2_database_update(url):
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

    dota2_team_list = []  # Creating team list for API

    # Inserting Match detail to table:

    o = 1
    u = 0

    for values in range(15):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        sql_insert = 'UPDATE DOTA2_MATCHES SET TEAMS = %s, TIME_IST = %s, Last_updated = %s WHERE _INDEX = %s'
        val = (
            str(f'{final_team_list[u][0]} VS {final_team_list[u][1]}'), str(dota2_time.dota2_time[u]),
            str(current_time),
            str(o))
        e = str(f'{final_team_list[u][0]} VS {final_team_list[u][1]}')
        dota2_team_list.append(e)
        database.mycursor.execute(sql_insert, val)
        database.mydb.commit()
        o += 1
        u += 1

    print(f'DOTA2 Matches Schedule Updated successfully!')
    # logger.info('dota2_matches_ran_successfully')

    # Merging Match names with time of Matches and converting it in a dictionary
    dota2_dict = dict(zip(dota2_team_list, dota2_time.dota2_time))
