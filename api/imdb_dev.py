import requests
IMDB_API_BASE = "https://api.imdbapi.dev"
url = f"{IMDB_API_BASE}/search/titles"
query = "only you"
respinse = requests.get(
    url ,
    params = { "query": query},
    timeout = 10
)
if respinse.status_code == 200:
    data = respinse.json()
    titleid = data["titles"][0]["id"]
    print(titleid)
    new_url = f"{IMDB_API_BASE}/titles/{titleid}/seasons"
    print(new_url)
    episodes = requests.get(
        new_url,
    )
    if episodes.status_code == 200:
        episode = episodes.json()
        print(episode)
    else:
        print(f"status code: {episodes.status_code}")
        # call other api