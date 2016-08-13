# coding: UTF-8
import pandas as pd
import csv
import urllib2
from bs4 import BeautifulSoup
import lxml
import evaluate_pred as ep

def get_race_list():
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    return years.tolist()


def scraping(url, output_file):
    # read page source code
    f = open('./../Data/' + output_file, 'w')
    csvWriter = csv.writer(f)
    soup = BeautifulSoup(urllib2.urlopen(url), "lxml")
    # Extract status
    title = soup.find('h1')
    print title.text

    table = soup.find(class_='race_table_01 nk_tb_common')
    for tr in table.findAll('tr',''):
        list = []
        for td in tr.findAll('td',''):
            word = " ".join(td.text.rsplit())
            list.append( word.encode('utf-8') )
        # print list
        csvWriter.writerow(list)
    f.close()

def scrape_res(url, output_file):
    # read page source code
    f = open('./../Data/res_'+ output_file, 'w')
    csvWriter = csv.writer(f)
    soup = BeautifulSoup(urllib2.urlopen(url), "lxml")

    table = soup.find(class_='pay_block')
    for tr in table.findAll('tr',''):
        list = []
        th = tr.find('th').string
        list.append(th.encode('utf-8'))
        for td in tr.findAll('td',''):
            if td.string == None:
                td = td.get_text(separator=' ')
                # print td.encode('utf-8')
                list.append(td.encode('utf-8'))
            else:
                # print(td.string.encode('utf-8'))
                list.append(td.string.encode('utf-8'))
        csvWriter.writerow(list)
    f.close()

if __name__ == '__main__':
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    for year in years:
        print year
        year = str(year)
        url = 'http://db.netkeiba.com/race/' + year + '/'
        output_file = year + '.csv'
        # scrape race data
        html_doc = scraping(url, output_file)
        # scrape rate data
        res_doc = scrape_res(url, output_file)
        # normalize rate data
        ep.normalize_race_odds()
