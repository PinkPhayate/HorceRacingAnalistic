import csv, re, lxml, urllib2
from bs4 import BeautifulSoup
def scrape_today(rid):
    # read page source code
    output_file = rid + '.csv'
    f = open('./../Data/Today/' + output_file, 'w')
    csvWriter = csv.writer(f)

    src = './../' + rid + '_src'
    soup = BeautifulSoup(open(src), "lxml")
    table = soup.find(class_='race_table_01 nk_tb_common shutuba_table')

    for tr in table.findAll('tr',''):
        list = []
        for td in tr.findAll('td',''):
            # get race status
            word = " ".join(td.text.rsplit())
            print word.encode('utf-8')
            list.append( word.encode('utf-8') )

            # get hid
            for link in td.findAll('a'):
                url = link.attrs['href']
                if "race" in link.attrs['href']:
                    tmp = url.split('/')
                    list.append(tmp[4])
        csvWriter.writerow(list)

if __name__ == '__main__':
    rid = '201601020511'
    scrape_today(rid)
