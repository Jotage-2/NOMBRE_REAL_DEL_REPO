#!/bin/bash 
gunicorn -b 0.0.0.0:5000 cajero_flask:app 
gunicorn -b 0.0.0.0:5000 cajero_flask:app 
