import calendar

to_date = list(map(int, input().split(' ')))
cur_day = (calendar.weekday(to_date[2], to_date[0], to_date[1]))
print(calendar.day_name[int(cur_day)].upper())
