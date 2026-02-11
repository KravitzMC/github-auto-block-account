import json5
import requests
from datetime import datetime
from loader import load_config

config = load_config()

Token = config["Token"]
Keyword = config["Keyword"]

followers = []
page = 1
per_page = 500

# Login
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {Token}",
}

me = requests.get("https://api.github.com/user", headers=headers).json()
my_login = me["login"]


# Get user followers
while True:
    url = f"https://api.github.com/users/{my_login}/followers"
    params = {
        "per_page": per_page,
        "page": page
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    if not data:
        break

    followers.extend(data)
    page += 1    

print("Anti spam bot followers for Github")
print(f"Login as : {my_login}, Total followers: {len(followers)}")
print("_" * 70)
print("Scaning spam bot users .....")

# Start block spam bot users
for u in followers:
    login = u['login']
    response = requests.get(f"https://api.github.com/users/{u['login']}",headers=headers)   
    data = response.json()

    if Keyword.casefold() in str(data.get('bio')).casefold():        
        response = requests.put(f"https://api.github.com/user/blocks/{u['login']}", headers=headers)

        if response.status_code == 204:            
            print(f"found account : {data['login']} reason → {data.get('bio')}  [Action] --> Blocked")      


print(f"Done !!!")

