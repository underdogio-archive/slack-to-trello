#!/usr/bin/env bash
# Exit upon first failure
set -e

# If there is no `slack_to_trello/config/env`, complain and leave
if ! test -f slack_to_trello/config/env; then
  echo "\`slack_to_trello/config/env\` doesn't exist." 1>&2
  echo "Please follow the instructions in our README to create a copy." 1>&2
  exit 1
fi

# Inherit our environment from the `env` file
. slack_to_trello/config/env

# Run our script
python slack_to_trello/__init__.py
