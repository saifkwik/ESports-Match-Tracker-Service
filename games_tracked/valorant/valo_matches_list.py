import requests
from bs4 import BeautifulSoup
from datetime import datetime
from games_tracked.valorant import valo_time_list
from db import database


# from dateutil.tz import gettz
# from utils.logs_handler import create_logger

# logger = create_logger(__name__, remote_logging=False)
def valo_update_database(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    # To get match list of 15 teams:
    i = 0
    c = []
    b = soup.find_all('div', class_='h-match-team-name')
    for names in range(30):
        c.append(b[i].get_text().replace('\n', '').replace('\t', ''))
        i += 1

    # Pairing teams together:
    n = 2
    teams = [c[i:i + n] for i in range(0, len(c), n)]

    # To get final list of Matches with timing:
    final_match_list = []
    p = 0
    for final in teams:
        j = list(teams[p] + list(valo_time_list.final_time_list[p]))
        final_match_list.append(j)
        p += 1

    # Inserting Match detail to table:

    api_team_list = []  # Creating team list for API

    o = 1
    for values in final_match_list:
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        sql_insert = 'UPDATE VALORANT_MATCHES SET TEAMS = %s, TIME_LEFT = %s, Last_updated = %s WHERE _INDEX = %s'
        val = (str(f'{values[0]} VS {values[1]}'), str(values[2]), str(current_time), str(o))
        q = str(f'{values[0]} VS {values[1]}')
        api_team_list.append(q)
        # print(f'{values[0]} VS {values[1]} at {values[2]}')
        database.mycursor.execute(sql_insert, val)
        database.mydb.commit()
        o += 1

    print(f'Valorant Matches Schedule Updated successfully!')
    # logger.info('valo_matches_ran_successfully')

    # Merging Match names with time of Matches and converting it in a dictionary
    valorant_dict = dict(zip(api_team_list, valo_time_list.time_strings))
