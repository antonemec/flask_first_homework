import random
import string
# import requests
import csv
import sqlite3

from sqlite_funct import exec_query
from faker import Faker
from flask import Flask, request

app = Flask('app')
fake = Faker()

'''
def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=',')
    len_rows = 0
    s_height = 0
    s_weight = 0
    for line in reader:
        len_rows += 1
        s_height += float(line[' "Height(Inches)"'])
        s_weight += float(line[' "Weight(Pounds)"'])
    av_height = round(s_height / len_rows, 2)
    av_weight = round(s_weight / len_rows, 2)
    return f'height: {av_height} <br>weight: {av_weight}'
'''

@app.route('/')
def main():
    return """<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8" />
  <title>HomeWork - Python</title>
 </head>
 <body>
  <a href="http://127.0.0.1:5001/limit_symbols?num_sym=100"><b>Open limit_symbols</a>
  <br>
  <br>
  <a href="http://127.0.0.1:5001/customers_location?Country=Brazil&City=Stuttgart"><b>Open customers_location</b></a>
  <br>
  <br>
  <a href="/customers_uniq"><b>Open customers_uniq</b></a>
  <br>
  <br>
  <a href="/invoice_items"><b>Open invoice_items</b></a>
 </body>
</html>
"""


@app.route('/limit_symbols')
def limit_symbols():
    a = int(request.args['num_sym'])
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(a))


@app.route('/customers_location')
def customers_location():
    a = request.args['Country']
    b = request.args['City']
    query = (f'select * '
             f'from customers '
             f'where Country = \'{a}\' '
             f'or City = \'{b}\'' 
             f';')
    result = exec_query(query)
    return str(result)


@app.route('/customers_uniq')
def customers_uniq():
    query = (f'select distinct FirstName '
             f'from customers'
             f';')
    result = exec_query(query)
    return str(result)


@app.route('/invoice_items')
def invoice_items():
    query = (f'select sum(UnitPrice * Quantity) as "SUM_ALL"  '
             f'from invoice_items'
             f';')
    result = exec_query(query)
    return str(result)


if __name__ == '__main__':
    app.run(port=5001)  # выбираем куда припарковать в localhost
