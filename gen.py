import requests
import json

headers = {"Content-type": "application/json", "Accept": "text/plain"}
url = "http://localhost:9090/api/event"

data = {
    "intervalStartDate": "2023-10-09 23:00:00",
    "intervalMinutes": 10,
    "trxCount": 10,
}
r = requests.post(url, data=json.dumps(data), headers=headers)
status = r.status_code
result = r.json()
for e in result:
    print(e["clientIPAddress"])
