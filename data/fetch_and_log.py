# fetch_and_log.py
import requests, json, os
from datetime import datetime

url = "https://realtime-weather-api-1.onrender.com/data"
filename = "data/history.json"

# Fetch data
r = requests.get(url)
data = r.json()
data['fetched_at'] = datetime.now().isoformat()

# Tạo folder nếu chưa có
os.makedirs("data", exist_ok=True)

# Đọc dữ liệu cũ
if os.path.exists(filename):
    with open(filename, 'r') as f:
        try:
            history = json.load(f)
        except:
            history = []
else:
    history = []

# Thêm dữ liệu mới
history.append(data)

# Ghi lại
with open(filename, 'w') as f:
    json.dump(history, f, indent=2)
