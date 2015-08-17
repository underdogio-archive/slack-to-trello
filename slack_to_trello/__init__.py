# Load in our dependencies
import os

from flask import Flask, request

from slack_to_trello.model import SLACK_TOKEN, make_trello_card, send_slack_message

# Start up a server
app = Flask(__name__)


# Set up our endpoints
@app.route('/')
def root():
    """Reply to curious persons"""
    return 'slack-to-trello made by Underdog.io with love <3'


@app.route('/slack/message', methods=['POST'])
def slack_message():
    """When we receive a message from Slack, generate a Trello card and reply"""
    # Incoming request format:
    # token=TOKEN
    # team_id=T0001
    # team_domain=example
    # channel_id=C12345
    # channel_name=test
    # user_id=U12345
    # user_name=Steve
    # command=/weather
    # text=94070

    # Verify Slack token lines up
    if request.form['token'] != SLACK_TOKEN:
        return ('Provided Slack token from message didn\'t match our server\'s Slack token. '
                'Please double check they are aligned', 403)

    # Extract our text and make a card
    text = request.form['text']
    user_name = request.form['user_name']
    # Pre-emptively extract channel name before taking actions (transaction-esque)
    channel_name = request.form['channel_name']
    card = make_trello_card(name='{text} ({user_name})'.format(text=text, user_name=user_name))

    # Send a message to Slack about our success
    # TODO: Escape our content
    send_slack_message(channel='#{channel_name}'.format(channel_name=channel_name),
                       text='Trello card "<{url}|{text}>" created by "{user_name}"'
                       .format(url=card.url, text=text, user_name=user_name))

    # Reply with nothing (as the external message does more)
    return ''


# If this is a direct invocation, start our server
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    env = os.environ.get('ENV', 'development')
    app.debug = env != 'production'
    app.run(port=port)
