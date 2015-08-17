#!/usr/bin/env bash
# Exit upon first failure
set -e

# Allow for skipping lint during development
if test "$SKIP_LINT" != "TRUE"; then
  flake8 *.py bin/ slack_to_trello/
fi

# Inherit our test environment variables
. slack_to_trello/config/env.test

# Run our tests
nosetests $* slack_to_trello/test/*.py
