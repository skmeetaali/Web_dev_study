import requests
from datetime import date, datetime
base = "https://www.episodate.com/api"

shoe = "2gether the series"

url = f"{base}/search"

response = requests.get(
    url, 
    params= {"q":shoe},
    timeout=10
)    

if response.status_code == 200:
    data = response.json()
    id = data["tv_shows"][0]["id"]
    url = f"{base}/show-details"  
    tv_show = data["tv_shows"][0]
    title = tv_show["name"]
    status = tv_show["status"]
    thumbnail_img = tv_show["image_thumbnail_path"]
    print(thumbnail_img)
    
    season = 2
        
    response = requests.get(
        url,
        params={"q":id},
        timeout=10
    )
    
    if response.status_code == 200:
        show_details = response.json()
        episodes = show_details["tvShow"]["episodes"]
        print(f"Show details: {show_details}")
        max_season = 0
        if tv_show["status"] == "Running":
            for ep in episodes:
                if ep["season"] == season:
                    date = ep["air_date"]
                    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                    ep_date = date.date()
                    if ep_date > date.today().date():
                        next_ep_release_date = ep_date
                        next_ep_no = ep["episode"]
                        last_released_ep = next_ep_no - 1
                        break
                    
                if ep["season"] > int(season):
                    last_released_ep = 0
                    for ep in episodes:
                        if ep["season"] == season:
                            if last_released_ep < ep["episode"]:
                                last_released_ep = ep["episode"]
                    break
                    
            for ep in episodes:
                if ep["season"] > max_season:
                    max_season = ep["season"]
                                
        elif tv_show["status"] == "Ended":
            last_released_ep = 0
            next_ep_release_date = None
            for ep in episodes:
                if ep["season"] > max_season:
                    max_season = ep["season"]
            for ep in episodes:
                if ep["season"] == max_season:
                    if last_released_ep < ep["episode"]:
                        last_released_ep = ep["episode"]
                    
                        
        if status == "Ended":
            total_ep = last_released_ep
        else:
            total_ep = None
        
        print(max_season)
        print(f"last released {last_released_ep}")
        print(f"next rel date{next_ep_release_date}")