import requests

query = """
query {
  title(id: "tt0944947") {
    primaryTitle

    episodes {
      episodes {
        episode
        season
        titleText
      }
    }
  }
}
"""

response = requests.post(
    "https://api.imdbapi.dev/graphql",
    json={"query": query}
)

print(response.json())