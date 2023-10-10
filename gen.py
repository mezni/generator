import requests
import json
from datetime import datetime, timedelta
from confluent_kafka import Producer

headers = {"Content-type": "application/json", "Accept": "text/plain"}
url = "http://localhost:9090/api/event"

data = {
    "intervalStartDate": "2023-10-09 23:00:00",
    "intervalMinutes": 5,
    "trxCount": 5,
}

conf = {'bootstrap.servers': '172.18.0.3:9092'}
producer = Producer(conf)


r = requests.post(url, data=json.dumps(data), headers=headers)
status = r.status_code
result = r.json()

#for e in result:
#    print(e["clientIPAddress"])
#    producer.produce('events', json.dumps(e).encode('utf-8'))
#    producer.flush()


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
#    else:
#        print("Message produced: %s" % (str(msg)))


#for e in result:
#    print(e["clientIPAddress"])
#    producer.produce('events', value=json.dumps(e).encode('utf-8'), callback=acked)
#    producer.poll(1)


start_date="2023-10-10 18:00:00"
duration_in_minutes=5
transactions_per_minutes=1000

start_date_time = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
for i in range(duration_in_minutes):
    next_start_date_time = start_date_time + timedelta(minutes = i)
    next_start_date=next_start_date_time.strftime('%Y-%m-%d %H:%M:%S')
    j=0
    while j<transactions_per_minutes:
        request_data = {
            "intervalStartDate": next_start_date,
            "intervalMinutes": 1,
            "trxCount": 100,
        }
        
        r = requests.post(url, data=json.dumps(data), headers=headers)
        status = r.status_code
        result = r.json()

        for e in result:
            producer.produce('events', value=json.dumps(e).encode('utf-8'), callback=acked)
            producer.poll(1)
            j=j+1
            print (j)