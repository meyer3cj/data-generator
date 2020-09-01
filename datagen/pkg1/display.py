import csv
from datetime import datetime
import calendar
import random as rnd
import numpy as np

with open("people.csv", 'r', newline='')as csvread:
    reader = csv.reader(csvread)
    sales = []
    next(reader)
    people=[]
    for row in reader:
        namecol= row[0]
        if namecol not in people:
            people.append(namecol)

    csvread.close()


