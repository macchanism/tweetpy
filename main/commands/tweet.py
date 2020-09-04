#! /usr/bin/env python

"""ツイートする"""
# 参考[1] https://qiita.com/bakira/items/00743d10ec42993f85eb

#標準のjsonモジュールとconfig.pyの読み込み
import json, config
#OAuthのライブラリの読み込み
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
#認証処理
twitter = OAuth1Session(CK, CS, AT, ATS)

#ツイートポストエンドポイント
url = "https://api.twitter.com/1.1/statuses/update.json"

print("内容を入力してください。")
#キーボード入力の取得
tweet = input('>> ')
print('*******************************************')

params = {"status" : tweet}

#post送信
res = twitter.post(url, params = params)

if res.status_code == 200:
#正常投稿出来た場合
    print("Success.")
else:
#正常投稿出来なかった場合
    print("Failed. : %d"% res.status_code)
