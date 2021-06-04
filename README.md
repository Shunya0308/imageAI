# Machine Learning

①画像認識/imageAI
画像(image.jpg)をGoogle APIを使いどの要素が含まれているかを自動判別して表示する機能。

言語:python

使用ライブラリ
・google.cloud

使用API
・Vision API

画像をimageに保存　→ image画像をAPIで解析　→ 解析結果をターミナル画面で表示

②Flaskを使ったLINE勤怠管理Bot/app.py
LINEで出勤・退勤と送信したらその時刻でスプレッドシートに出勤時間、退勤時間を書き込み、書き込みが終わったらLINEで返信する

使用言語:python

使用ライブラリ
・pandas
・linebot
・gspread
・フレームワーク → Flask
・インフラ → Heroku

LINEからのメッセージを取得　→ その文字を判定して（出勤か退勤かそれ以外か）　→ 時刻をそれに応じたスプレッドシートの列に挿入　→ 書き込みが完了したらLINEで登録完了したことを返信



