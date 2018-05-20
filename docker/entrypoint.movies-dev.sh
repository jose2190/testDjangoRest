#!/bin/bash
pip install --upgrade virtualenv
PYTHON3PATH=$(which python3)
VIRTUALENVBIN=$(which virtualenv)
VIRTUALENVPATH='/home/movies/venv'
mkdir -p $VIRTUALENVPATH
$VIRTUALENVBIN -p $PYTHON3PATH $VIRTUALENVPATH
source $VIRTUALENVPATH/bin/activate && pip install -r /home/movies/code/requeriments.txt
source $VIRTUALENVPATH/bin/activate && cd /home/movies/code/ && python manage.py migrate
source $VIRTUALENVPATH/bin/activate && cd /home/movies/code/ && python manage.py runserver 0.0.0.0:8000
