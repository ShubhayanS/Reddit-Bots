import praw
import re
import time

reddit = praw.Reddit(client_id='ZdBLJ46S9PW-DA',
                     client_secret='LeZ_YY6vI1aN1WmI5gpO_-T3mwM',
                     user_agent='<console:reddit_bot:0.0.1 (by /u/yt_vid_bot)',
                     username='shubhayans',
                     password='mynameiskhan1')

#print(reddit.read_only)
subreddits = ['programmerhumour', 'funny', 'memes','mildlyinteresting']
pos = 0

title = 'Funny programmer joke'
url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRQQQkOoakOTX8dR7Qb2hkpsnzQD_15Bj8CC1u273VAE_pI0eRH'

def post():
    global subreddits
    global pos

    subreddit = reddit.subreddit(subreddits[pos])
    subreddit.submit(title, url=url)

    pos = pos + 1

    if(pos >= len(subreddits) - 1):
        post()
    else:
        print ("Done")

post()
