#!/usr/bin/python3
"""index.py to connect to API"""
import app_views from api.v1.views


@app_views.route('/status')
def hbnbStatus():
    """hbnbStatus"""
    return ('{\n\t"status": "OK"\n}')

@app_views.route('/api/v1/stats')
def hbnbStats():
    """hbnbStats"""
    storage.count()
