import requests
from bs4 import BeautifulSoup
from games_tracked.cs import cs_time_list
from datetime import datetime
from db import database


# from dateutil.tz import gettz
# from utils.logs_handler import create_logger
#
# logger = create_logger(__name__, remote_logging=False)

def cs_database_update(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    divTag = soup.find_all('div', class_='mlist col-md-8')

    a = []
    x = 0
    for tag in divTag:
        v = tag.find_all("span", class_="tn1")
        for teams in v:
            a.append(v[x].get_text().replace('\n', '').replace('\t', ''))
            x += 1

    team1_strings = a[0:15]

    t = 1
    team1_list = [team1_strings[i:i + t] for i in range(0, len(team1_strings), t)]

    b = []
    x = 0
    for tag in divTag:
        v = tag.find_all("span", class_="tn2")
        for teams in v:
            b.append(v[x].get_text().replace('\n', '').replace('\t', ''))
            x += 1

    team2_strings = b[0:15]

    y = 1
    team2_list = [team2_strings[i:i + y] for i in range(0, len(team2_strings), y)]

    cs_team_list = []  # Creating team list for API

    # Inserting Match detail to table:
    o = 1
    u = 0
    for values in range(15):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        if cs_time_list.time_list[u][0] == '':
            cs_time_list.time_list[u][0] = 'Finished'
        sql_insert = 'UPDATE CS_MATCHES SET TEAMS = %s, TIME_IST = %s, Last_updated = %s WHERE _INDEX = %s'
        val = (
            str(f'{team1_list[u][0]} VS {team2_list[u][0]}'), str(cs_time_list.time_list[u][0]), str(current_time),
            str(o))
        e = str(f'{team1_list[u][0]} VS {team2_list[u][0]}')
        cs_team_list.append(e)
        database.mycursor.execute(sql_insert, val)
        database.mydb.commit()
        o += 1
        u += 1
    print(f'Counter Strike Matches Schedule Updated successfully!')
    # logger.info('cs_matches_ran_successfully')

    # Merging Match names with time of Matches and converting it in a dictionary
    cs_dict = dict(zip(cs_team_list, cs_time_list.time_strings))
