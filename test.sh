#!/usr/bin/env bash
# Exit upon first failure
set -e

# Allow for skipping lint during development
if test "$SKIP_LINT" != "TRUE"; then
  flake8 *.py slack_to_trello/
fi

# Run our tests
nosetests $* slack_to_trello/test/*.py
