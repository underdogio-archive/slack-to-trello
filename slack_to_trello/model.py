# Load in our dependencies
import os
import json

import httplib2
from trello import Board, List, TrelloClient

# Verify we have all our environment variables
# DEV: We keep all of these settings here as it could be dynamic based on request in the future
SLACK_TOKEN = os.environ['SLACK_TOKEN']
SLACK_MESSAGE_URL = os.environ['SLACK_MESSAGE_URL']
TRELLO_API_KEY = os.environ['TRELLO_API_KEY']
TRELLO_TOKEN = os.environ['TRELLO_TOKEN']
TRELLO_BOARD_ID = os.environ['TRELLO_BOARD_ID']
TRELLO_LIST_ID = os.environ['TRELLO_LIST_ID']

# Generate a Trello client
trello_client = TrelloClient(
    api_key=TRELLO_API_KEY,
    token=TRELLO_TOKEN,
)


def make_trello_card(*args, **kwargs):
    """Generate a new Trello card"""
    # Generate our card board and list
    # DEV: board is never used...
    # TODO: This is very backwards with needing a board to get a client...
    #   Might move to another lib
    # https://github.com/sarumont/py-trello/blob/0.4.3/trello/trellolist.py#L11-L20
    # https://github.com/sarumont/py-trello/blob/0.4.3/trello/trellolist.py#L48-L63
    board = Board(client=trello_client, board_id=TRELLO_BOARD_ID)
    card_list = List(board=board, list_id=TRELLO_LIST_ID)
    return card_list.add_card(*args, **kwargs)


def send_slack_message(channel, text):
    """Send a message to Slack"""
    http = httplib2.Http()
    return http.request(SLACK_MESSAGE_URL, 'POST', body=json.dumps({
        'channel': channel,
        'text': text,
    }))
