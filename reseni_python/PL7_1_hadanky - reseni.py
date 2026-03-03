#Start code here
import requests
import time
api_url = "https://riddles-api.vercel.app/random"
odpoved = requests.get(api_url)
hadanka = odpoved.json()["riddle"]
reseni = odpoved.json()["answer"]
print(hadanka)
time.sleep(6)
print(reseni)
