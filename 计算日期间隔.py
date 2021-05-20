import time
start_date = "2020-1-1"
end_date = "2021-1-1"

start_sec = time.mktime(time.strptime(start_date, '%Y-%m-%d'))
end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))

days = (end_sec - start_sec) / 86400

print(days)
