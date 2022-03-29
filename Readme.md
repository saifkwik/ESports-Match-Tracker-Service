# ESports-Matches-Tracker :
This API gives you information of upcoming/ongoing tournament matches of Valorant, Counter Strike and Dota2. It scrapes
data from Internet Gaming sites using Beautiful Soup and Selenium .

## Match-Tracker BOT (telegram-Bot) :
Based on the App this Bot fetches data from API and displays result in the telegram app.
*  www.t.me/ESports_match_tracker_bot

## API Installation
* clone the repo and type ` uvicorn api_match_tracker:app --reload` in the terminal directory.
* * `pip install requirements.txt`
* Open 127.0.0.1:8000 in the Browser.



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
