# -*- coding: utf-8 -*-
"""
Created on Mon May 10 22:12:26 2021

@author: yaobv
"""
import pandas as pd
import json
import requests

URL = 'https://raw.githubusercontent.com/LambdaSchool/Django-RPG/master/testdata.json'
file = requests.get(URL)


data = json.loads(file.text)

