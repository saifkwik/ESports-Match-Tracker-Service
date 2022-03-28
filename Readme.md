# ESports-Matches-Tracker :
This API gives you information of upcoming/ongoing tournament matches of Valorant, Counter Strike and Dota2. It scrapes
data from Internet Gaming sites using Beautiful Soup and Selenium .



## Installation


* clone the repo and type `uvicorn main:app --reload` in the terminal directory.
* * `pip install requirements.txt`
* Open 127.0.0.1:8000 in the Browser.



## Usage


Run 
`http://127.0.0.1:8000/valorant?match_index='(Enter number of matches info you want to view (max<15))'`,
`http://127.0.0.1:8000/dota2?match_index='(Enter number of matches info you want to view (max<15))'`,
`http://127.0.0.1:8000/cs?match_index='(Enter number of matches info you want to view (max<15))'` to :
* Get list of Ongoing and Upcoming matches sorted with their time.


![alt text](https://github.com/saifkwik/api_esports_matches/blob/main/Screenshot-1.png)

![alt text](https://github.com/saifkwik/api_esports_matches/blob/main/Screenshot-2.png)
