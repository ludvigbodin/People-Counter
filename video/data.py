# -*- coding: utf-8 -*-
import datetime
import json

# Writing and reading from/to json files
def get_record_from_file():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data

def save_tracking_to_file(inOrOut):
    record = get_record_from_file()
    today = datetime.datetime.today().strftime('%Y-%m-%d') # 2019-10-31
    hour = datetime.datetime.now().hour
    key = str(hour) + "-" + str(hour+1) # 11-12

    if today not in record:
        record[today] = {}
    if key not in record[today]:
        record[today][key] = {}
    if inOrOut not in record[today][key]:
        record[today][key][inOrOut] = 0

    time_object = record[today][key].copy()
    time_object[inOrOut] = time_object[inOrOut] + 1

    record[today][key] = time_object
    with open("data.json", "w") as out:
        json.dump(record, out)

def get_total_today():
    record = get_record_from_file()
    today = datetime.datetime.today().strftime('%Y-%m-%d') # 2019-10-31

    if today not in record:
        return 0
    stats = record[today]

    totalIn = 0
    totalOut = 0
    print(stats)

    for time_period in stats:
        totalIn += stats[time_period]["in"] if "in" in stats[time_period] else 0
        totalOut += stats[time_period]["out"] if "out" in stats[time_period] else 0
    return totalIn - totalOut
