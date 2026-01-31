#7.  Convert a date given as a string to a date/datetime type in Python.
from datetime import datetime
date="2026-01-31 10:30:00"
res=datetime.strptime(date,"%Y-%m-%d %H:%M:%S")
print(res)
print(type(res))