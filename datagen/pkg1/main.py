import csv
from datetime import datetime
import calendar
import random as rnd
import numpy as np

months = []
years = []
styear = 2000
for i in range(21):
    n = styear
    years.append(n)
    styear += 1
print(years)
for i in range(1, 12):
    print(calendar.month_name[i])
    months.append(calendar.month_name[i])
names = []
jan = datetime.date


def getrndmonth():
    return months[rnd.randint(0, len(months) - 1)]


def getrndyear():
    return years[rnd.randint(0, len(years) - 1)]


def getrndname():
    return names[rnd.randint(0, len(names) - 1)]


def getsalesamt():
    return rnd.randint(150, 8000)


with open("names.csv", newline='')as namesfile:
    reader = csv.reader(namesfile)
    for row in reader:
        n = row[1]
        names.append(n)
    print(names)
    namesfile.close()

with open("people.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Name", "Month", "Year", "Sale Amount"])
    runs =8000
    for i in range(runs):
        writer.writerow([getrndname(), getrndmonth(), getrndyear(), getsalesamt()])
    csvfile.close()

with open("people.csv", 'r', newline='')as csvread:
    reader = csv.reader(csvread)
    sales = []
    next(reader)
    for row in reader:
        intadd = int(row[3])
        sales.append(intadd)
    avgsale1=round(np.mean(sales),2)
    avgsale=avgsale1
    year=0
    print(sales)
    print(avgsale)


