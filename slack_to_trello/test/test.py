from unittest import TestCase
from slack_to_trello import slack_to_trello


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(slack_to_trello.run))
