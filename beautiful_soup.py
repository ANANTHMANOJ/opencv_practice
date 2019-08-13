# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 11:22:39 2019

@author: AmNayak
"""
import requests
from bs4 import BeautifulSoup
from csv import DictWriter
resp=requests.get("http://www.canaraengineering.in/")
html=resp.text
html=BeautifulSoup(html,"html.parser")
print(html)

with open("college.csv",'w') as file:
    full=["text"]
    csv_wrt= DictWriter(file,fieldnames=full)
    csv_wrt.writeheader()
    csv_wrt.writerow(dict(html))
