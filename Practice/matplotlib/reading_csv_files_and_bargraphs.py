from matplotlib import pyplot as plt
import csv
from collections import Counter

plt.style.use('fivethirtyeight')

with open('data.csv') as file:
    csv_reader = csv.DictReader(file) # generates a dictionary iterator

    lc = Counter()
    # row = next(csv_reader)      # gives next element of the iterator    
    
    for row in csv_reader:
        lc.update(row['LanguagesWorkedWith'].split(';'))

lang = []
fcount = []

for data in lc.most_common(15):
    lang.append(data[0])
    fcount.append(data[1])

plt.barh(lang, fcount)

plt.title("Most popular languages")
# plt.xlabel('Programming Language')
plt.xlabel('Frequency')

plt.tight_layout()
plt.show()