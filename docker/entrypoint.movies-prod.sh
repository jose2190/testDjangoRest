#!/bin/bash
pip install --upgrade virtualenv
PYTHON3PATH=$(which python3)
VIRTUALENVBIN=$(which virtualenv)
VIRTUALENVPATH='/home/movies/venv'
mkdir -p $VIRTUALENVPATH
$VIRTUALENVBIN -p $PYTHON3PATH $VIRTUALENVPATH
source $VIRTUALENVPATH/bin/activate && pip install -r /home/movies/code/requeriments.txt
source $VIRTUALENVPATH/bin/activate && cd /home/movies/code/ && python manage.py migrate
source $VIRTUALENVPATH/bin/activate && pip install gunicorn
$VIRTUALENVPATH/bin/gunicorn movies.wsgi --bind 0.0.0.0:8000 -w 10 --graceful-timeout 350 -t 350
