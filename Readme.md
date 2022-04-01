# ESports-Matches-Tracker :
This API gives you information of upcoming/ongoing tournament matches of Valorant, Counter Strike and Dota2. It scrapes
data from Internet Gaming sites using Beautiful Soup and Selenium .

## Match-Tracker BOT (telegram-Bot) :
Based on the App this Bot fetches data from API and displays result in the telegram app.
*  www.t.me/ESports_match_tracker_bot


![alt text](https://github.com/saifkwik/api_esports_matches/blob/main/screenshots/api_esports_matches.png)

## API Installation
* clone the repo and type ` uvicorn api_match_tracker:app --reload` in the terminal directory.
* * `pip install requirements.txt`
* Open 127.0.0.1:8000 in the Browser.

## Data Crawler Function installation in Docker :

* Uncomment the lines in 
* * db_update.py 
* *  cs_matches_list.py
* *  cs_time_list.py
* *  valo_matches_list.py
* * dota2_matches_list.py 
* *  dota2_time_list.py
* and change your MySQL logging info in database.py
* docker build -t db-update .
* docker run --network bridge  -p 8000:8000 -v logs:/match-tracker/api_esports_matches/logs db-update 




## Usage
### ESports Matches Tracker Bot <br/>
Start conversation with `/start` <br/>
*`/valo` ~ To get Valorant matches <br/>
*`/cs` ~ To get Counter Strike matches <br/>
*`/dota2` ~ To get Dota2 matches <br/>


### API Run <br/>
`http://127.0.0.1:8000/valo?match_index='(Enter number of matches info you want to view (max<15))'`,<br/>
`http://127.0.0.1:8000/dota2?match_index='(Enter number of matches info you want to view (max<15))'`,<br/>
`http://127.0.0.1:8000/cs?match_index='(Enter number of matches info you want to view (max<15))'` to :
* Get list of Ongoing and Upcoming matches sorted with their time.


![alt text](https://github.com/saifkwik/api_esports_matches/blob/main/screenshots/Screenshot-1.png)

![alt text](https://github.com/saifkwik/api_esports_matches/blob/main/screenshots/Screenshot-2.png)
