from games_tracked.valorant.valo_matches_list import valo_update_database
from games_tracked.cs.cs_matches_list import cs_database_update
from games_tracked.dota2.dota2_match_list import dota2_database_update
import time
from concurrent.futures import ThreadPoolExecutor

valo_url = 'https://vlr.gg'
cs_url = 'https://ggscore.com/en/csgo/matches'
dota2_url = 'https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches'

urls = [valo_url, cs_url, dota2_url]


def games_function(urls):
    if urls == "https://vlr.gg":
        valo_update_database(valo_url)
    if urls == "https://ggscore.com/en/csgo/matches":
        cs_database_update(cs_url)
    if urls == "https://liquipedia.net/dota2/Liquipedia:Upcoming_and_ongoing_matches":
        dota2_database_update(dota2_url)


def main():
    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(games_function, urls)


if __name__ == '__main__':
    main()

time = time.perf_counter()
print(f'Time taken: {time} seconds')
