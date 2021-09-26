#!/bin/bash
python3 manage.py runserver 0.0.0.0:8000 &
P1=$!
mongod &
P2=$!
wait $P1 $P2
