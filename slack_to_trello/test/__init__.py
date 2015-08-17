# Load in our dependencies
import json
from unittest import TestCase

import mock

from slack_to_trello import app


# Define our tests
class SlackToTrelloTestCase(TestCase):
    def setUp(self):
        """Start a server to test on"""
        self.app = app.test_client()

    def test_root(self):
        """
        A request to /
            receives a response from the server
        """
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)

    @mock.patch('slack_to_trello.model.List')
    @mock.patch('httplib2.Http.request')
    def test_slack_message(self, request_mock, trello_list_mock):
        """
        A POST request to /slack/message
            triggers a Trello card creation
            triggers a Slack message to a channel
            replies but with no content
        """
        # Define our mocks
        add_card_mock = trello_list_mock().add_card
        add_card_mock().url = 'http://trello.url/'

        # Make our request
        res = self.app.post('/slack/message', data={
            'token': 'token_from_slash_commands',
            'team_id': 'T0001',
            'team_domain': 'example',
            'channel_id': 'C12345',
            'channel_name': 'test',
            'user_id': 'U12345',
            'user_name': 'twolfson',
            'command': '/trello',
            'text': 'This is a test card',
        })
        self.assertEqual(res.status_code, 200)

        # Assert mock data
        # DEV: If HTTP data gets too complex to test, consider using httpretty-fixtures
        # DEV: 1 count for our initial setup, 1 for actual invocation
        self.assertEqual(add_card_mock.call_count, 2)
        self.assertEqual(add_card_mock.call_args[1]['name'], 'This is a test card (twolfson)')

        self.assertEqual(request_mock.call_count, 1)
        self.assertEqual(request_mock.call_args[0][1], 'POST')
        self.assertEqual(json.loads(request_mock.call_args[1]['body']), {
            'channel': '#test',
            'text': 'Trello card "<http://trello.url/|This is a test card>" created by "twolfson"',
        })
