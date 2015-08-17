#!/usr/bin/env python
# Load in our auth utility from py-trello
# https://github.com/sarumont/py-trello/blob/0.4.3/trello/util.py
from trello.util import create_oauth_token


# Run our script
if __name__ == '__main__':
    create_oauth_token(name='slack-to-trello', scope='read,write', expiration='never')
