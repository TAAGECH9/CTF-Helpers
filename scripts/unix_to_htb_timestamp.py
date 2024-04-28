import datetime

timestamp_str = input("Enter the timestamp: ")

timestamp_seconds = float(timestamp_str)
utc_datetime = datetime.datetime.utcfromtimestamp(timestamp_seconds)

print("Time in UTC is:", utc_datetime)
