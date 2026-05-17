import requests

Tv_maze_root = "https://api.tvmaze.com"
anilist_root = "https://graphql.anilist.co"
query = """
query ($search: String) {

Media(search: $search, type: ANIME) {

    bannerImage

    coverImage {
    extraLarge
    large
    medium
    color
    }

    nextAiringEpisode {
    episode
    airingAt
    timeUntilAiring
    }

    airingSchedule {
    nodes {
        episode
        airingAt
    }
    }

    title {
    native
    english
    }

    status
    popularity
    episodes
}
}
"""

name = "one piece"
variables = {
    "search": name
}

response = requests.post(
    anilist_root,
    json={
        "query" : query,
        "variables": variables

    }
)

data = response.json()
media = data["data"]["Media"]
title = media["title"]["english"]
original_title = media["title"]["native"]
total_ep = media["episodes"]
status = media["status"]
thumbnail_img = media["coverImage"]["medium"]
next_airing = media["nextAiringEpisode"]
if next_airing:
    last_released_ep = next_airing["episode"] - 1
    next_ep_release_date = next_airing["airingAt"]
else:
    last_released_ep = media["episodes"]
    next_ep_release_date = None

if media:
    print(title, original_title, next_ep_release_date, last_released_ep, thumbnail_img, total_ep)
    print(thumbnail_img)


