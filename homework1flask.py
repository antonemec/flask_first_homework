import random
import requests
import csv
from faker import Faker
from flask import Flask

app = Flask('app')
fake = Faker()


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


@app.route('/')
def main():
    return """<!DOCTYPE html>
<html>
 <head>
  <meta charset="utf-8" />
  <title>HomeWork - Python</title>
 </head>
 <body>
  <a href="/requirements"><b>Open requirements</a>
  <br>
  <br>
  <a href="/mails"><b>Open mails</b></a>
  <br>
  <br>
  <a href="/avgmass"><b>Open avgmass</b></a>
  <br>
  <br>
  <a href="/astros"><b>Open astros</b></a>
 </body>
</html>
"""


@app.route('/requirements')
def requirements():
    a = list()
    with open('requirements.txt', encoding='utf-8') as f:
        for raw_line in f:
            a.append(raw_line.strip())
    return "<br>".join(a)


@app.route('/mails')
def mails():
    base = list()
    a = 0
    mails = ['@gmail.com', '@yahoo.com', '@i.ua', '@fb.com', '@zapos.com', '@ya.ru', '@ukr.net', '@mail.ru', '@gov.ua',
             '@rambler.ru', '@bk.ru', '@hotbox.ru', '@yahoo.com', '@hotmail.com', '@msn.com']
    year = ['80', '81', '82', '85', '88', '95', '91', '93', '17', '2019', '18', '1998', '1980', '1997', '2005', '2000',
            '05', '06', '13', '2015', '2014', '2010', '2008', '2007']
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    dest = ['.', '_']
    while a < 100:
        a += 1
        b = fake.first_name()
        c = fake.last_name()
        base.append(
            f"{a}|    |{b + ' ' + c}|    |{b + c + random.choice(month) + random.choice(dest) + random.choice(year) + random.choice(mails)}")
    return "<br>".join(base)


@app.route('/avgmass')
def avgmass():
    with open("hw.csv") as f_obj:
        answer = csv_dict_reader(f_obj)
        answer = str(answer)
        return answer


@app.route('/astros')
def astro_api():
    url = "http://api.open-notify.org/astros.json"
    r = requests.get(url)
    astro_data = r.json()
    num = astro_data['number']
    return f'{num} астронавтов в космосе'


if __name__ == '__main__':
    app.run(port=5001)
