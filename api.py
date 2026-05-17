import requests

API_KEY = 'bb8bca8b23c3cd367e4427c2e163e971'
BASE_URL = "https://api.themoviedb.org/3"

headers = {
    "accept": "application/json"
}
movie = '10 dance'


params = {
    "api_key": API_KEY,
    "query": movie
}

def fetch_pop_movies():
    try:
        url = f'{BASE_URL}/search/movie?api_key={API_KEY}&query={movie}'
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            first_movie = data["results"][0]
            title = first_movie["title"]
            overview = first_movie["overview"]
            print(data)
            print(f"Title :{title} \nOverview : {overview}")
        else:
            print("error fetching data")
    except Exception as e :
        print("exception", e)
        
if __name__ == '__main__':
    fetch_pop_movies()