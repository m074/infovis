import pandas as pd
from datetime import datetime, timedelta
import csv

sexos = {}
df = pd.read_csv('w40.csv')

for row in df.values:
    sex, age, *b = row
    if sex not in sexos:
        sexos[sex] = b
    else:
        sexos[sex] = [sum(x) for x in zip(sexos[sex],b)]

out_csv = open('processed.csv', 'w', newline='')
fieldnames = ['sex', 'year','pop']
writer = csv.DictWriter(out_csv, fieldnames=fieldnames)
writer.writeheader()



for k,v in sexos.items():
    for y,vv in zip(range(2011,2051),v):
        writer.writerow({'sex':k,'year':y,'pop':vv})
