#coding: utf-8

import mysql.connector
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time


# 各種設定
# DB設定
config = {
    "user": "pizero",
    "password": "H01SMwjWZTFZB41H",
    "host": "localhost",
    "port": 3306,
    "database": "succeedling",
    "raise_on_warnings": True,
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(dictionary=True)


# SQLのフォーマット
register_temps = ("INSERT INTO temps "
                    "(inside_temp, outside_temp) "
                    "VALUES (%(inside_temp)s, %(outside_temp)s)")



# センサーの設定 (もう一個のセンサーのID:3c01e0761dd6)
#inside_sensor = W1ThermSensor(sensor_id="3c01e0761e16")
#outside_sensor = W1ThermSensor(sensor_id="3c01e0767e5b")


# 気温の取得
#inside_temp = inside_sensor.get_temperature()
#outside_temp = outside_sensor.get_temperature()

inside_temp = 8.333
outside_temp = 12.777


f = open('temps.txt', 'a')
f.write(dt_now.strftime('%Y年%m月%d日 %H:%M:%S') + " inside:" + str(inside_temp) + ", outside:" + str(outside_temp) >
f.close()


# DBへの登録
###

