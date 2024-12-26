import requests
headers = { "x-apisports-key": "6732a3d212744481c28f836db783c293"}
url = "https://v3.football.api-sports.io/teams"
response = requests.get(url, headers=headers)
data = response.json()
print(data)