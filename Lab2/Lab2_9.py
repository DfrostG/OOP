day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month, year):
    day_of_years = 0
    if is_leap(year) and month > 2:
        day_of_years += 1
    else:
      if month == 2 and day == 29:
        return -1
    for i in range(month):
        day_of_years += day_in_month[i]
    day_of_years += day
    return day_of_years

def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 365

def date_diff(date1, date2):
    date1 = [int(d) for d in date1.split("-")]
    date2 = [int(d) for d in date2.split("-")]
    if (date1[1] > 12 or date1[1] < 1 or date2[1] > 12 or date2[1] < 1):
        return -1
    elif (date1[0] == 29 and date1[1] == 2 and not is_leap(date1[2])) or (date2[0] == 29 and date2[1] == 2 and not is_leap(date2[2])):
        return -1
    elif (date1[0] > day_in_month[date1[1]] or date1[0] < 0) or (date2[0] > day_in_month[date2[1]] or date2[0] < 0):
        return -1
    else:
        return sum([day_in_year(i) for i in range(date1[2], date2[2])]) + (day_of_year(date2[0], date2[1], date2[2])) - (day_of_year(date1[0], date1[1], date1[2])) + 1
