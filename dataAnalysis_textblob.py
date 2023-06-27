'''
Description: this is a program of analyzing the data collected from twitter. textblob library is used.

Authors: Zequan Tang,

Date: June 22, 2023
'''

import csv
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt

positive = 0
negative = 0
neutral = 0
total = 0
data = []

with open("./tweets_Job.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    # get the content
    content = row[2]            
    if(str(content) == 'Content'):
      continue
    text = content.replace('\n', ' ')
    
    # sentimental analysis and counting
    blob = TextBlob(text)
    sa = TextBlob(str(blob))
    
    # print(sa.sentiment.polarity, "\n")
    if (sa.sentiment.polarity > 0):
      positive += 1
      tuple1 = (text, 'Will not replace')
      data.append(tuple1)
    
    if (sa.sentiment.polarity == 0):
      neutral += 1
      tuple2 = (text, 'Neutral')
      data.append(tuple2)

    if (sa.sentiment.polarity < 0):
      negative += 1
      tuple3 = (text, 'Will replace')
      data.append(tuple3)

# write back to a csv file
fileName = 'dataTextblob.csv'
with open(fileName, 'w', newline='') as csvfile:
        header = ['Content', 'Result']
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)

# data visualization
categories = ['Will not replace', 'Neutral', 'Will replace']
data = [positive, neutral, negative]
colors = ['#F08080', '#68838B', '#BFEFFF']

def func(pct, data):
    absolute = int(pct / 100.*np.sum(data))
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.pie(data, explode=None, labels=categories, colors=colors, startangle=90,radius = 1.2, autopct=lambda pct: func(pct, data), shadow=True)
plt.title("Distribution of 5,000 Twitter users' opinions on whether AI will replace human jobs in the future (by TextBlob)")
plt.legend()
plt.show()