#Start code here
import requests
odpoved = requests.get("https://catfact.ninja/fact")
print(odpoved.status_code)
if odpoved.status_code == 200:
  nahodny_fakt = odpoved.json()["fact"]
  print(nahodny_fakt)
