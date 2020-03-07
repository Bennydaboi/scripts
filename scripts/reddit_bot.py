import praw
import time
import urllib
import os

reddit = praw.Reddit(client_id='D_wijuRjCcn8vA',
		client_secret="7u79-Z_2cWVUqoGTAPiKcO6a3PM",
		password='9665792181',
		user_agent='rpi-test by /u/bennyboiiii',
		user_name='bennyboiiii')

subreddit = reddit.subreddit('rabbits')

#print(subreddit.display_name)
#print(subreddit.title)
#print(subreddit.description)

for submission in subreddit.hot(limit=10):
#	print(submission.title)
	print(submission.score)
#	print(submission.id)
#	print(submission.url)

urllib.urlretrieve(submission.url, '/home/pi/scripts/local.jpg')

os.system("python /home/pi/scripts/telegram_sendphoto.py")
