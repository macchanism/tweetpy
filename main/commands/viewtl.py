#! /usr/bin/env python

"""タイムラインを取得"""
# 参考[1] https://qiita.com/bakira/items/00743d10ec42993f85eb
# 参考[2] https://qiita.com/orange_u/items/3f0fb6044fd5ee2c3a37

#標準のjsonモジュールとconfig.pyの読み込み
import json, config
#OAuthのライブラリの読み込み
from requests_oauthlib import OAuth1Session

import sys
args = sys.argv

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
#認証処理
twitter = OAuth1Session(CK, CS, AT, ATS)

#タイムライン取得エンドポイント
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#取得数
if len(args) != 1:
    c = int(args[1])
else:
    c = 5
params = {'count' : c}
res = twitter.get(url, params = params)

if res.status_code == 200:
#正常通信出来た場合
    #レスポンスからタイムラインリストを取得
    timelines = json.loads(res.text)
    #タイムラインリストをループ処理
    for line in timelines:
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else:
#正常通信出来なかった場合
    print("Failed: %d" % res.status_code)
