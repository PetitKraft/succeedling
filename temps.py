#coding: utf-8

from __future__ import print_function

from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import datetime
import time



# SpreadSheet用設定
SPREADSHEET_ID = '1WV3AqBbdljhG5gHZrR5qXJZwm_o5UhImrV27Vmyec9M'
RANGE_NAME = 'Data!A2:C'
VALUE_INPUT_OPTION = "USER_ENTERED"



def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = service_account.Credentials.from_service_account_file("service_account_credentials.json")
        



    """センサーの設定
       3c01e0761dd6: 短い,無印
       3c01e0761e16: 長い,黄色線1本
       3c01e0767e5b: 長い,黄色線2本"""
    outside_sensor = W1ThermSensor(sensor_id="3c01e0761dd6")
    inside_sensor1 = W1ThermSensor(sensor_id="3c01e0767e5b")
    #inside_sensor2 = W1ThermSensor(sensor_id="3c01e0761e16")



    # モータードライバー用の設定
    #lwin_lpwm = 24
    #lwin_rpwm = 23
    #rwin_lpwm = 22
    #rwin_rpwm = 27
    #GPIO.setmode(GPIO.BOARD)
    #GPIO.setup(lwin_lpwm,GPIO.OUT)
    #GPIO.setup(lwin_rpwm,GPIO.OUT)
    #GPIO.setup(rwin_lpwm,GPIO.OUT)
    #GPIO.setup(rwin_rpwm,GPIO.OUT)



    # 気温の取得
    measured_at = datetime.datetime.now().isoformat()
    outside_temp = outside_sensor.get_temperature()
    inside_temp1 = inside_sensor1.get_temperature()
    inside_temp2 = 80#inside_sensor2.get_temperature()



    # 気温に基づいてサイドビニールの開け閉め
    #if inside_temperature =    
    #    GPIO.output(lwin_lpwm, isUp)
    #    GPIO.output(lwin_rpwm, not(isUp))
    #    GPIO.output(rwin_lpwm, not(isUp))
    #    GPIO.output(rwin_rpwm, isUp)


    
    try:
        service = build('sheets', 'v4', credentials=creds)

        values = [
            [
                measured_at, outside_temp, inside_temp1, inside_temp2
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

        print('Datetime, Outside, Inside1, Inside2:')
        for row in values:
            print('%s, %s, %s, %s' % (row[0], row[1], row[2], row[3]))

    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
