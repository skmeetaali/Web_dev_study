import requests
from datetime import date, datetime
base = "https://www.episodate.com/api"

shoe = "fake fact lips"

url = f"{base}/search"

response = requests.get(
    url, 
    params= {"q":shoe},
    timeout=10
)
if response.status_code == 200:
    data = response.json()
    print(data)
    id = data["tv_shows"][0]["id"]
    url = f"{base}/show-details"    
    response = requests.get(
        url,
        params={"q":id},
        timeout=10
    )
    if response.status_code == 200:
        show_details = response.json()
        episodes = show_details["tvShow"]["episodes"]
        for ep in episodes:

            date = ep["air_date"]
            date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            date_only = date.date()
            if date_only > date.today().date():
                print(ep)
else:
    print(response.status_code)