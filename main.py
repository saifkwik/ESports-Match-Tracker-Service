import time
from Valorant import valo_matches_list
from cs import cs_matches_list
from fastapi import FastAPI

print('DATABASE UPDATED')

app = FastAPI()


@app.get('/')
def root():
    link = f'http://127.0.0.1:8000/valorant',f'http://127.0.0.1:8000/cs'
    return link


@app.get('/valorant')
def root(match_index):
    valo_matches_list.mycursor.execute(f'SELECT Last_Updated FROM game_database.VALORANT_MATCHES limit 1')
    valo_last_updated = f'Updated at {valo_matches_list.mycursor.fetchall()} time'

    valo_matches_list.mycursor.execute(f'SELECT TEAMS, TIME_LEFT FROM game_database.VALORANT_MATCHES '
                                       f'LIMIT {match_index}')
    _val = valo_matches_list.mycursor.fetchall()
    return valo_last_updated, _val


@app.get('/cs')
def root(match_index):
    cs_matches_list.mycursor.execute(f'SELECT Last_Updated FROM game_database.CS_MATCHES limit 1')
    cs_last_updated = f'Updated at {cs_matches_list.mycursor.fetchall()} time'
    cs_matches_list.mycursor.execute(f'SELECT TEAMS, TIME_IST FROM game_database.CS_MATCHES limit {match_index}')
    _cs = cs_matches_list.mycursor.fetchall()
    return cs_last_updated, _cs


t1 = time.perf_counter()
print(f'Time taken: {t1} seconds')
