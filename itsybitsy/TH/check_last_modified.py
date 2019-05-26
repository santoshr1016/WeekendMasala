import os
import datetime


def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(t)

filename = "bazooka.py"
diff_time = datetime.datetime.now() - modification_date(filename)
print(int(diff_time.total_seconds()))