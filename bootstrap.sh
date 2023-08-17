#!/bin/sh
export FLASK_APP=./app.py
pipenv run flask --debug run -h localhost -p 5000