'''Question 4 -
Write a program to download the data from the link given below and then read the data and convert the into
the proper structure and return it as a CSV file.
Link - https://data.nasa.gov/resource/y77d-th95.json
Note - Write code comments wherever needed for code understanding.
Sample Data -
Excepted Output Data Attributes
● Name of Earth Meteorite - string id - ID of Earth
● Meteorite - int nametype - string recclass - string
● mass - Mass of Earth Meteorite - float year - Year at which Earth
● Meteorite was hit - datetime format reclat - float recclong - float
● point coordinates - list of int'''

import requests
import csv
import pandas as pd

# Download the data from the URL
url = "https://data.nasa.gov/resource/y77d-th95.json"
response = requests.get(url)
data = response.json()

# Extract the required information from the data
csv_data = []

for item in data:
    csv_row = {
        "Name": item.get("name", ""),
        "id": item.get("id", ""),
        "nametype": item.get("nametype", ""),
        "recclass": item.get("recclass", ""),
        "mass": item.get("mass (g)", ""),
        "year": item.get("year", ""),
        "reclat": item.get("reclat", ""),
        "reclong": item.get("reclong", ""),
        "geolocation": f"{item.get('reclat', '')}, {item.get('reclong', '')}"
    }
    csv_data.append(csv_row)

# Create a DataFrame from the extracted data
df1 = pd.DataFrame(csv_data)

# Save the DataFrame to an csv file
output_file = "NASA.csv"
df1.to_csv(output_file, index=False)

print("Data has been converted and saved to", output_file)