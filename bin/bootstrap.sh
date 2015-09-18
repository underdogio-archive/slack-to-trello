#!/usr/bin/env bash
# Exit on the first error
set -e

# If there is no virtualenvwrapper, install it
if ! compgen -c | grep virtualenvwrapper &> /dev/null; then
  sudo pip install virtualenvwrapper
  echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
  source /usr/local/bin/virtualenvwrapper.sh
fi

# Create and activate a virtual environment to work on
# DEV: For performance purposes, we keep our virtualenv outside of `/vagrant/`
# If we can't jump to `slack-to-trello` virtualenv and aren't yet in a virtualenv
#   (we get an error for jumping to the current virtual env), then create `slack-to-trello`
if ! workon slack-to-trello &> /dev/null && test -z "$VIRTUAL_ENV"; then
  mkvirtualenv slack-to-trello
fi

# Install its dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Add this repo as a library
python setup.py develop
