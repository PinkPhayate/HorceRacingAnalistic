# coding: UTF-8
import pandas as pd
import csv,re,json
if __name__ == '__main__':
    df = pd.read_csv('./../Data/race_info.csv', header=None)
    years = df[9]
    odds_dict = {}
    for year in years:
        y = str(year)
        output_file = y + '.csv'
        f = open('./../Data/res_'+ output_file, 'rb')
        dataReader = csv.reader(f)
        dict = {}
        for row in dataReader:
            odds = row[2]
            if ' ' in odds:
                odds = odds.split('　')
            num = row[1].replace('→','-')
            num = num.replace(' - ','-')
            if ' ' in num:
                num = num.split('　')
            dict[row[0]] = {'num':num,'odds': row[2]}

        odds_dict[y] = dict
    f = open("./../Data/odds_dict.json", "w")
    json.dump(odds_dict, f, ensure_ascii=False)
