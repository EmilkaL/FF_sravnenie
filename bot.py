import head_logic
from pprint import pprint

import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials


# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'creds.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = '1RYNJkDqSG5zbUmYgdVdZxloWTyD6MS2nIjhV9rvutZ4'

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
students = head_logic.main()
values = service.spreadsheets().values().batchUpdate(
    spreadsheetId=spreadsheet_id,
    body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "B2" + ":E" +str(len(students)+1) ,
             "majorDimension": "ROWS",
             "values": students}
	]
    }
).execute()
body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "G3",
             "majorDimension": "ROWS",
             "values": [str(len(students))]},
	]
    }
