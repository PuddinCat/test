import requests

r = requests.get("https://github.com")

with open("result.txt", "w") as f:
    f.write(str(r.status_code))
