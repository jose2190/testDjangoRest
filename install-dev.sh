#!/bin/bash
PYTHON3PATH=$(which python3)
VIRTUALENVBIN=$(which virtualenv)
VIRTUALENVPATH='venv'
mkdir -p $VIRTUALENVPATH
$VIRTUALENVBIN -p $PYTHON3PATH $VIRTUALENVPATH
source $VIRTUALENVPATH/bin/activate && pip install -r movies/requeriments.txt
source $VIRTUALENVPATH/bin/activate && cd movies && python manage.py migrate
