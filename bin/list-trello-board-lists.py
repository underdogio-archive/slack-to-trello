#!/usr/bin/env python
# Load in our dependencies
from __future__ import print_function
import argparse

from trello import Board, TrelloClient


# Define our logic
def main(api_key, token, board_id):
    """List out the board lists for our client"""
    trello_client = TrelloClient(
        api_key=api_key,
        token=token,
    )
    board = Board(client=trello_client, board_id=board_id)
    print('Lists')
    print('-----')
    print('Name: Id')
    for card_list in board.all_lists():
        print('{card_list.name}: {card_list.id}'.format(card_list=card_list))


# Run our script
if __name__ == '__main__':
    # Set up our parser
    parser = argparse.ArgumentParser(description='Output list ids for a Trello board')
    parser.add_argument('api_key', help='Key used for TRELLO_API_KEY in env')
    parser.add_argument('token', help='Token used for TRELLO_TOKEN in env')
    parser.add_argument('board_id', help='Id of board (taken from `list-trello-boards.py`)')

    # Parse and run via kwargs
    args = parser.parse_args()
    main(**args.__dict__)
