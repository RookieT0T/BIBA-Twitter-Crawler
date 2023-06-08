'''
Description: this is a web scraping program of twitter.
             Codes are based on https://github.com/israel-dryer/Twitter-Scraper written by Israel Dryer and some modifications are made.

Authors: Israel Dryer, Zequan Tang, 

Date: June 07, 2023

How to run: locate this program in terminal, run this program with python3, enter required information and a csv file will be 
generated automatically. Please make sure selenium and python3 have been installed before running this program.
'''

import csv
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

def parseData(post):
    # get userName
    name = post.find_element("xpath", './/span').text

    # get date
    try:
        date = post.find_element("xpath", './/time').get_attribute('datetime')
    except NoSuchElementException:
        return
    
    # get content
    content = post.find_element("xpath", './/div[1]/div[1]/div[2]/div[2]/div[2]').text
    # check if the tweet is replying to someone.
    # if it does, move to .../div[3] to read the content of the tweet
    if content.startswith('Replying to'):
        content = post.find_element("xpath", './/div[1]/div[1]/div[2]/div[2]/div[3]').text
    
    # get reply count
    replyCnt = post.find_element("xpath", './/div[@data-testid="reply"]').text
    if replyCnt == '':
        # set none to default value 0
        replyCnt = '0'
        
    # get retweet count
    retweetCnt = post.find_element("xpath", './/div[@data-testid="retweet"]').text
    if retweetCnt == '':
        # set none to default value 0
        retweetCnt = '0'
        
    # get like count
    likeCnt = post.find_element("xpath", './/div[@data-testid="like"]').text
    if likeCnt == '':
        # set none to default value 0
        likeCnt = '0'
    
    # create a tuple and fill its values
    tweet = (name, date, content, replyCnt, retweetCnt, likeCnt)
    return tweet

# ask for username, email, topic, password, and number of tweets
userName = input('Enter your username: ')
email = input('Enter your email address: ')
topic = input('Enter your topic: ')
password = getpass('Enter your password: ')
valid = False
while not(valid):
    num = input('Approximately how many tweets you want to collect: ')
    if num.isdigit():
        valid = True

# use Chrome as the default browser
driver = Chrome()

# open twitter
driver.get('https://twitter.com/i/flow/login')
driver.maximize_window()
sleep(35)

# enter email and next
emailAddr = driver.find_element("xpath", '//input[@name="text"]')
emailAddr.send_keys(email)
emailAddr.send_keys(Keys.RETURN)
sleep(10)

# enter name and next
try:
    name = driver.find_element("xpath", '//input[@name="text"]')
    name.send_keys(userName)
    name.send_keys(Keys.RETURN)
    sleep(10)
# check if we need to enter username this time
except NoSuchElementException:
    print("Don't need to enter username this time. Keep waiting.")

# enter password and next
passwords = driver.find_element("xpath", '//input[@name="password"]')
passwords.send_keys(password)
passwords.send_keys(Keys.RETURN)
#sleep(15)

# search the topic
sleep(40)
searchLabel = driver.find_element("xpath", '//input[@aria-label="Search query"]')
searchLabel.send_keys(topic)
searchLabel.send_keys(Keys.RETURN)
sleep(30)
driver.find_element("link text", 'Latest').click()
sleep(30)

data = []
tweet_ids = set()
last_position = driver.execute_script("return window.pageYOffset;")
scrolling = True
enough = False

while scrolling:
    try:
        posts = driver.find_elements("xpath", '//article[@data-testid="tweet"]')    # read all tweets on the current page and store
                                                                                    # them as a list
        for post in posts[-15:]:
            tweet = parseData(post)     # parse the tweets
            if tweet:
                tweet_id = ''.join(tweet)
                if tweet_id not in tweet_ids:
                    tweet_ids.add(tweet_id)
                    data.append(tweet)
                    if(len(data) >= int(num)):   # check if enough data has been collected
                        enough = True
                        break
        
        if enough == True:
            break
        scroll_attempt = 0
        while True:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(10)
            curr_position = driver.execute_script("return window.pageYOffset;")
            if last_position == curr_position:
                scroll_attempt += 1
                
                # end of scroll region
                if scroll_attempt >= 3:
                    scrolling = False
                    break
                else:
                    sleep(10) # attempt another scroll
            else:
                last_position = curr_position
                break
    except:
        break
driver.close()

# create a csv file and write data into the file
with open('tweets.csv', 'w', newline='', encoding='utf-8') as f:
    header = ['Username', 'Time', 'Content', 'Reply Count', 'Retweet Count', 'Like Count']
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)