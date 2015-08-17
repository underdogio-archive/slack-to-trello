#!/usr/bin/env bash
# Exit upon first failure
set -e

# Load in our parameters
channel="$1"
if test "$channel" = ""; then
  echo "We require a channel name (e.g. \"engineering\", excluding the \"#\") in order to send a fake message to your organization." 1>&2
  echo "Please provide one as a parameter. For example, if your test channel is \`bot-test\`, then use:" 1>&2
  echo "bin/fake-slack-message.sh bot-test" 1>&2
  exit 1
fi

# Generate content for our fake Slack message
body="token=TOKEN"
body="$body&team_id=T0001"
body="$body&team_domain=example"
body="$body&channel_id=C12345"
body="$body&channel_name=$channel"
body="$body&user_id=U12345"
body="$body&user_name=Steve"
body="$body&command=/trello"
body="$body&text=This is a test card"
curl --include http://localhost:5000/slack/message -X POST --data "$body"
