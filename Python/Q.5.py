"""Question 5 Write a program to download the data from the given API link and then extract the following data with
proper formatting
Link - http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes
Note - Write proper code comments wherever needed for the code understanding
Sample Data -
Excepted Output Data Attributes -
● id - int url - string
● name - string season
● - int number - int
● type - string airdate -
● date format airtime -
● 12-hour time format
● runtime - float
● average rating - float
● summary - string
● without html tags
● medium image link - string
● Original image link - string"""


import requests
import json
from bs4 import BeautifulSoup

# Download the data from the URL
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = json.loads(response.text)

# Extract the required information from the data
show_id = data.get("id", "")
show_url = data.get("url", "")
show_name = data.get("name", "")

episodes = data.get("_embedded", {}).get("episodes", [])
episode_data = []

for episode in episodes:
    episode_id = episode.get("id", "")
    episode_url = episode.get("url", "")
    episode_season = episode.get("season", "")
    episode_number = episode.get("number", "")
    episode_type = episode.get("type", "")
    episode_airdate = episode.get("airdate", "")
    episode_airtime = episode.get("airtime", "")
    episode_runtime = episode.get("runtime", "")
    episode_rating = episode.get("rating", {}).get("average", "")
    episode_summary = episode.get("summary", "")

    # Remove HTML tags from the episode summary using BeautifulSoup
    episode_summary = BeautifulSoup(episode_summary, "html.parser").get_text()

    episode_image_medium = episode.get("image", {}).get("medium", "")
    episode_image_original = episode.get("image", {}).get("original", "")

    # Create a dictionary for the episode data
    episode_dict = {
        "id": episode_id,
        "url": episode_url,
        "name": show_name,
        "season": episode_season,
        "number": episode_number,
        "type": episode_type,
        "airdate": episode_airdate,
        "airtime": episode_airtime,
        "runtime": episode_runtime,
        "average rating": episode_rating,
        "summary": episode_summary,
        "medium image link": episode_image_medium,
        "original image link": episode_image_original
    }

    # Append the episode dictionary to the list
    episode_data.append(episode_dict)

# Save the data to a file
output_file = "westworld_episodes.json"

with open(output_file, mode="w", encoding="utf-8") as file:
    json.dump(episode_data, file, indent=4)

print("Data has been extracted and saved to", output_file)