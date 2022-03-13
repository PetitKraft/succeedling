from __future__ import print_function

from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime


SPREADSHEET_ID = '1WV3AqBbdljhG5gHZrR5qXJZwm_o5UhImrV27Vmyec9M'
RANGE_NAME = 'Data!A2:C'
VALUE_INPUT_OPTION = "USER_ENTERED"


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = service_account.Credentials.from_service_account_file("service_account_credentials.json")
    
    try:
        service = build('sheets', 'v4', credentials=creds)

        measured_at = datetime.datetime.now().isoformat()
        inside_temp = 12.555
        outside_temp = 19.588

        values = [
            [
                measured_at, inside_temp, outside_temp
            ],
        ]
        
        body = {
            'values': values
        }
        
        result = service.spreadsheets().values().append(
            spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
            valueInputOption=VALUE_INPUT_OPTION, body=body).execute()
        
        print('{0} cells appended.'.format(result
                                           .get('updates')
                                           .get('updatedCells')))

        if not values:
            print('No data found.')
            return

        print('Datetime, Inside, Outside:')
        for row in values:
            print('%s, %s, %s' % (row[0], row[1], row[2]))

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
