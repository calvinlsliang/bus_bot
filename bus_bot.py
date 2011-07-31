from twitter.api import Twitter, TwitterError
from twitter.oauth import OAuth, write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

import os
import time

oauth_filename = os.environ.get('HOME', '') + os.sep + '.twitter_oauth'
oauth_token, oauth_token_secret = read_token_file(oauth_filename)

cons_filename = os.environ.get('HOME', '') + os.sep + '.twitter_cons'
cons_key, cons_secret= read_token_file(cons_filename)

CONSUMER_KEY = 'c7f7YqJ0vFyL5z8lfwmAYw'
CONSUMER_SECRET = 'dvg5fupwTYJkt74zOVua6vUMV26KEITRyc1evvrZ40Q'

poster = Twitter( auth=OAuth(oauth_token, oauth_token_secret, cons_key, cons_secret),
		    secure=True,
		    api_version='1',
		    domain='api.twitter.com')

while (1):
    results = poster.statuses.mentions()
    if len(results) > 0:
	for result in results:
	    print 'User: ', result['user']['screen_name'], 'Message: ', result['text']
	    print 'Tweeting same message back to user'
	    new_status = result['text'].replace('@busbot1', '@'+result['user']['screen_name'])
	    poster.statuses.update(status = new_status)
    time.sleep(60)
	
