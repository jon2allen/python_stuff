from datetime import datetime, timedelta
import calendar


def get_next_month(month):
    i_month = month
    while True:
        if i_month == 12:
            i_month = 1
        else:
            i_month = i_month+1
        yield i_month


def get_prior_month(month):
    i_month = month
    while True:
        if i_month == 1:
            i_month = 12
        else:
            i_month = i_month-1
        yield i_month


def month_current_and_prior(month, count=1):
    if month == 0:
        time_t = datetime.now()
        current_month = time_t.month
    else:
        current_month = month
    g = get_prior_month(current_month)
    month_list = [current_month]
    for m in range(count):
        month_list.append(next(g))
    return month_list


def month_current_and_next(month, count=1):
    if month == 0:
        time_t = datetime.now()
        current_month = time_t.month
    else:
        current_month = month
    g = get_next_month(current_month)
    month_list = [current_month]
    for m in range(count):
        month_list.append(next(g))
    return month_list


time_t = datetime.now()

month = time_t.month

print("current ", month)

print(month_current_and_prior(0))

for x in range(1, 13):
    print(month_current_and_prior(x))

tst_month = 7


g = get_next_month(7)

print(next(g))
print(next(g))

for i in range(1, 13):
    print("month: ", next(g))

print(month_current_and_next(8, 12))

print(month_current_and_next(2))
print("current_and_prior")
month_lst = (month_current_and_next(7, 32))
print(month_current_and_prior(3))

for m in month_lst:
    print(calendar.month_name[m])
