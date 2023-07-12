import csv
import matplotlib.pyplot as plt

with open('./dataMerged.csv', 'r') as source_file:
    reader = csv.reader(source_file)
    next(reader)
    data = []
    num1 = 0
    num2 = 0
    num3 = 0

    num4 = 0
    num5 = 0
    num6 = 0

    num7 = 0
    num8 = 0
    num9 = 0

    num10 = 0
    num11 = 0
    num12 = 0

    num13 = 0
    num14 = 0
    num15 = 0

    num16 = 0
    num17 = 0
    num18 = 0

    num19 = 0
    num20 = 0
    num21 = 0

    num22 = 0
    num23 = 0
    num24 = 0

    num25 = 0
    num26 = 0
    num27 = 0

    num28 = 0
    num29 = 0
    num30 = 0

    num31 = 0
    num32 = 0
    num33 = 0

    num34 = 0
    num35 = 0
    num36 = 0

    num37 = 0
    num38 = 0
    num39 = 0

    for row in reader:
        
        list = row[1].split('-')
        month = int(list[1])
        date = int(list[2][0:2])
        
        if month == 6 and date == 18:
            if row[3] == 'Neutral':
                num1 += 1
            if row[3] == 'Will not replace':
                num2 += 1
            if row[3] == 'Will replace':
                num3 += 1
        
        if month == 6 and (date >= 11 and date < 18):
            if row[3] == 'Neutral':
                num4 += 1
            if row[3] == 'Will not replace':
                num5 += 1
            if row[3] == 'Will replace':
                num6 += 1

        if month == 6 and (date >= 4 and date < 11):
            if row[3] == 'Neutral':
                num7 += 1
            if row[3] == 'Will not replace':
                num8 += 1
            if row[3] == 'Will replace':
                num9 += 1

        if (month == 6 and (date >= 1 and date < 4)) or (month == 5 and (date >= 28 and date <= 31)):
            if row[3] == 'Neutral':
                num10 += 1
            if row[3] == 'Will not replace':
                num11 += 1
            if row[3] == 'Will replace':
                num12 += 1

        if month == 5 and (date >= 21 and date < 28):
            if row[3] == 'Neutral':
                num13 += 1
            if row[3] == 'Will not replace':
                num14 += 1
            if row[3] == 'Will replace':
                num15 += 1

        if month == 5 and (date >= 14 and date < 21):
            if row[3] == 'Neutral':
                num16 += 1
            if row[3] == 'Will not replace':
                num17 += 1
            if row[3] == 'Will replace':
                num18 += 1

        if month == 5 and (date >= 7 and date < 14):
            if row[3] == 'Neutral':
                num19 += 1
            if row[3] == 'Will not replace':
                num20 += 1
            if row[3] == 'Will replace':
                num21 += 1
        
        if (month == 5 and (date >= 1 and date < 7)) or (month == 4 and (date == 30)):
            if row[3] == 'Neutral':
                num22 += 1
            if row[3] == 'Will not replace':
                num23 += 1
            if row[3] == 'Will replace':
                num24 += 1

        if month == 4 and (date >= 23 and date < 30):
            if row[3] == 'Neutral':
                num25 += 1
            if row[3] == 'Will not replace':
                num26 += 1
            if row[3] == 'Will replace':
                num27 += 1

        if month == 4 and (date >= 16 and date < 23):
            if row[3] == 'Neutral':
                num28 += 1
            if row[3] == 'Will not replace':
                num29 += 1
            if row[3] == 'Will replace':
                num30 += 1

        if month == 4 and (date >= 9 and date < 16):
            if row[3] == 'Neutral':
                num31 += 1
            if row[3] == 'Will not replace':
                num32 += 1
            if row[3] == 'Will replace':
                num33 += 1

        if month == 4 and (date >= 2 and date < 9):
            if row[3] == 'Neutral':
                num34 += 1
            if row[3] == 'Will not replace':
                num35 += 1
            if row[3] == 'Will replace':
                num36 += 1

        if (month == 4 and date == 1) or (month == 3 and date == 31):
            if row[3] == 'Neutral':
                num37 += 1
            if row[3] == 'Will not replace':
                num38 += 1
            if row[3] == 'Will replace':
                num39 += 1

x = ['4.2 - 4.8', '4.9 - 4.15', '4.16 - 4.22', '4.23 - 4.29', '4.30 - 5.6', '5.7 - 5.13', '5.14 - 5.20', '5.21 - 5.27', '5.28 - 6.3', '6.4 - 6.10', '6.11 - 6.17']
y1 = [num34, num31, num28, num25, num22, num19, num16, num13, num10, num7, num4]
y2 = [num35, num32, num29, num26, num23, num20, num17, num14, num11, num8, num5]
y3 = [num36, num33, num30, num27, num24, num21, num18, num15, num12, num9, num6]

plt.plot(x, y1, color = '#FD5901', label = 'Neutral')
plt.plot(x, y2, color = '#FAAB36', label = 'Will not replace')
plt.plot(x, y3, color = '#008083', label = 'Will replace')

plt.xlabel('\nWeeks')
plt.ylabel('Number of tweets\n')
plt.title("Number of tweets in each category in weeks between March 31, 2023 and June 18, 2023\n")

plt.plot(y1, color = '#FD5901', linewidth = '2')
plt.plot(y2, color = '#FAAB36', linewidth = '2')
plt.plot(y3, color = '#008083', linewidth = '2')

plt.grid()
plt.legend()
plt.show()