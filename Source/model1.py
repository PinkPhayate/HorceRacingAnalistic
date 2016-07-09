import csv
import pandas as pd
import page_scraping as ps
着
順 	枠
番 	馬
番 	馬名 	性齢 	斤量 	騎手 	タイム 	着差 	ﾀｲﾑ
指数
	通過 	上り 	単勝 	人
気 	馬体重 	調教
ﾀｲﾑ
	厩舎
ｺﾒﾝﾄ
	備考
	調教師 	馬主 	賞金
(万円)
cols = ['rank', 'frame', 'num', 'name', 'sexAge', 'hande', 'jockey', 'time', 'diff', 'time_index', 'path', 'last', 'odds', 'fav', 'wight']
races = ps.get_race_list()
for race in races:

    df = pd.read_csv('./../Data/' + str(race) + '.csv', header=None)
    df = df.ix[:,0:14]
    df.columns = cols
