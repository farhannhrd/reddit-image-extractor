#!/usr/bin/env python
# coding: utf-8

# In[1]:

import praw
import pandas as pd
import datetime as dt
import requests
import urllib
import io
import ssl
import os


def main():

    username_login = input("Input your username here: ")
    password_login = input("Password here: ")

    reddit = praw.Reddit(client_id= os.environ.get('REDDIT_CLIENT_ID'),
                         client_secret= os.environ.get('REDDIT_CLIENT_SECRET'),
                         username=str(username_login),
                         password=str(password_login),
                         user_agent='test1')

    subred = input("Insert Subreddit Here")

    url_list = []
    limit_image = input("How many images do you want to extract?: ")
    time_period = input("Input your time period, month/week/day: ")

    subreddit = reddit.subreddit(str(subred))
    top_subreddit = subreddit.top(
        limit=int(limit_image), time_filter=str(time_period))
    for submission in top_subreddit:
        if not submission.stickied:
            print(submission.url)
            url_list.append(submission.url)

    try:
        image_dir = os.makedirs(f"reddit_imgs from {subred} subreddit")
    except:
        pass

    new_dir = os.getcwd() + f"/reddit_imgs from {subred} subreddit"

    os.chdir(new_dir)

    for url in url_list:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                with open(str(url)[-10:], 'wb') as file:
                    file.write(r.content)
        except:
            pass

    print(
        f"Extraction of {limit_image} images from r/{subred} for period of {time_period} is successful! Please check folder for images. ")

    # In[ ]:


main()
