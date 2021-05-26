import pandas as pd
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def auth():
    #秘密鍵指定
    SP_CREDENTIAL_FILE = 'secret.json'
    #APIの範囲指定
    SP_SCOPE = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive',
    ]

    #スプレッドシートのURLのd/以降をコピペ
    SP_SHEET_KEY = '1m2srseavfHJANTcvlfnrGyjYvAsMvL1W-Nra3Fd_zXs'
    #sheet名記載（任意）
    SP_SHEET = 'timesheet'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(SP_CREDENTIAL_FILE, SP_SCOPE)
    gc = gspread.authorize(credentials)

    worksheet = gc.open_by_key(SP_SHEET_KEY).worksheet(SP_SHEET)
    return worksheet

#出勤
def punch_in():
    worksheet = auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    date = timestamp.strftime('%Y/%m/%d')
    punch_in = timestamp.strftime('%H:%M')

    df = df.append({'日付': date, '出勤時間' : punch_in, '退勤時間': '00'}, ignore_index=True)

    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('勤怠（出勤）登録完了しました')

#退勤
def punch_out():
    worksheet =  auth()
    df = pd.DataFrame(worksheet.get_all_records())

    timestamp = datetime.now()
    punch_out = timestamp.strftime('%H:%M')

    df.iloc[-1, 2] = punch_out
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print('勤怠（退勤）登録完了しました')