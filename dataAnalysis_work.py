# '''
# Description: this is a program of analyzing the data collected from twitter. textBlob library is used.

# Authors: Zequan Tang,

# Date: June 21, 2023
# '''

import csv
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt

positive = 0
negative = 0
neutral = 0
total = 0
# num = 0

with open("./tweets2_Work.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    # get the content
    content = row[2]            
    if(str(content) == 'Content'):
      continue
    content.replace('\n', ' ')
    # get the like count
    likes = row[5]                 

    # '''
    # print(str(num) + ': ')
    # print(str(content), '\n')
    # '''
    # sentimental analysis and counting
    blob = TextBlob(content)
    sa = TextBlob(str(blob))
    
    if (sa.sentiment.polarity > 0):
      positive += 1
    
    if (sa.sentiment.polarity == 0):
      neutral += 1

    if (sa.sentiment.polarity < 0):
      negative += 1
    # num += 1

# '''
# print(str(positive), '\n')
# print(str(negative), '\n')
# print(str(neutral), '\n')
# '''

# data visualization
categories = ['Will work better', 'Neutral', 'Will not help work better']
data = [positive, neutral, negative]
colors = ['#F08080', '#68838B', '#BFEFFF']

def func(pct, data):
    absolute = int(pct / 100.*np.sum(data))
    return "{:.1f}%\n({:d})".format(pct, absolute)

plt.pie(data, explode=None, labels=categories, colors=colors, startangle=90,radius = 1.2, autopct=lambda pct: func(pct, data), shadow=True)
plt.title("Distribution of 168 Twitter users' opinions on whether chatGPT can make work better")
plt.legend()
plt.show()