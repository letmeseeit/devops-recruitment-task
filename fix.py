#! /usr/bin/env python3

import requests
from requests.exceptions import HTTPError
import os

def query_api(endpoint=''):
    try:
        response = requests.get(f'http://localhost:3000/{endpoint}')
        response.raise_for_status()
        json_response = response.json()["status"]
        print(f'Request {endpoint} successful, response: {json_response}')
        return json_response
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    

if __name__ == "__main__": 
    app = query_api()
    redis = query_api('redis')
    postgres = query_api('postgres')


    if app == "OK":
        if redis == "FAIL":
            os.system('docker-compose restart redis')
            print('Redis restarted')
        if postgres == "FAIL":
            os.system('docker-compose restart postgres')
            print('Postgres restarted')
    else:
        print('App is down')


