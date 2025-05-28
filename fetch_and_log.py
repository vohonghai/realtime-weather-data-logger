import requests, json, os
from datetime import datetime

url = "https://realtime-weather-api-1.onrender.com/data"
filename = "data/history.json"

r = requests.get(url)
data = r.json()
data['fetched_at'] = datetime.now().isoformat()

os.makedirs("data", exist_ok=True)

# Đọc file cũ nếu có
if os.path.exists(filename):
    with open(filename, 'r') as f:
        try:
            history = json.load(f)
        except:
            history = []
else:
    history = []

history.append(data)

with open(filename, 'w') as f:
    json.dump(history, f, indent=2)
