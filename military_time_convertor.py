"""
Author: R Santosh
Prob: Convert 12 hour clock to military time
"""


def get_am_pm(sec):
    pos = [i for i, e in enumerate(sec) if e.isalpha()]
    return int(sec[:pos[0]]), sec[pos[0]:]


def convert_24hr_military2(input_hour):
    hh, mm, ss = input_hour.split(':')
    ss, period = get_am_pm(ss)
    hh = int(hh)
    mm = int(mm)
    if period.upper() == 'PM' and hh < 12:
        hh = (hh + 12) % 24
    elif period.upper() == 'AM' and hh == 12:
        hh = (hh + 12) % 24
    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)


def convert_24hr_military(input_hour):
    hh, mm, ss = input_hour.split(':')
    ss, period = get_am_pm(ss)
    hh = int(hh) % 12

    if period.upper() == 'PM':
        hh = hh + 12

    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)

print(convert_24hr_military(input()))
