from fastapi import FastAPI
from db import database

description = """
ESports Matches Tracker API gives you information of Ongoing/Upcoming Mathces 🚀

## Games

* VALORANT
* COUNTER STRIKE
* DOTA-2

## URL

VALORANT, CS, DOTA2:
* ** http://127.0.0.1:8000/valo?match_index='(Enter number of matches info you want to view (max<15))'
* ** http://127.0.0.1:8000/cs?match_index='(Enter number of matches info you want to view (max<15))'
* ** http://127.0.0.1:8000/dota2?match_index='(Enter number of matches info you want to view (max<15))'
"""

app = FastAPI(
    title="ESports Matches Tracker API",
    description=description,
    version="1.0",
    contact={
        "name": "Saif Ahmad",
        "url": "https://github.com/saifkwik?",
        "email": "saifkwik@gmail.com",
    }
)


@app.get('/')
def root():
    link = f'http://127.0.0.1:8000/valo', f'http://127.0.0.1:8000/cs', f'http://127.0.0.1:8000/dota2'
    return link


@app.get('/valo')
def valorant(match_index):
    # valo_matches_list.mycursor.execute(f'SELECT Last_Updated FROM game_database.VALORANT_MATCHES limit 1')
    # valo_last_updated = f'Updated at {valo_matches_list.mycursor.fetchall()} time'

    database.mycursor.execute(f'SELECT TEAMS, TIME_LEFT FROM game_database.VALORANT_MATCHES '
                                       f'LIMIT {match_index}')
    _val = database.mycursor.fetchall()
    return _val


@app.get('/cs')
def root(match_index):
    # cs_matches_list.mycursor.execute(f'SELECT Last_Updated FROM game_database.CS_MATCHES limit 1')
    # cs_last_updated = f'Updated at {cs_matches_list.mycursor.fetchall()} time'
    database.mycursor.execute(f'SELECT TEAMS, TIME_IST FROM game_database.CS_MATCHES limit {match_index}')
    _cs = database.mycursor.fetchall()
    return _cs


@app.get('/dota2')
def root(match_index):
    # dota2_match_list.mycursor.execute(f'SELECT Last_Updated FROM game_database.DOTA2_MATCHES limit 1')
    # dota2_last_updated = f'Updated at {dota2_match_list.mycursor.fetchall()} time'
    database.mycursor.execute(f'SELECT TEAMS, TIME_IST FROM game_database.DOTA2_MATCHES limit {match_index}')
    _dota2 = database.mycursor.fetchall()
    return _dota2

print('API Started')

