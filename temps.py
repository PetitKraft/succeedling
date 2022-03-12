#coding: utf-8

import mysql.connector
#from w1thermsensor import W1ThermSensor
#import RPi.GPIO as GPIO
#import time


# DB設定
config = {
    "user": "pizero",
    "password": "bXkrWB5tJx4_AJb_",
    "host": "192.168.1.60",
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
inside_sensor = W1ThermSensor(sensor_id="3c01e0761e16")
outside_sensor = W1ThermSensor(sensor_id="3c01e0767e5b")


# 気温の取得
inside_temp = inside_sensor.get_temperature()
outside_temp = outside_sensor.get_temperature()


data = {
    "inside_temp": inside_temp,
    "outside_temp": outside_temp,
}


# DBへの挿入
cursor.execute(register_temps, data)


cursor.close()
cnx.commit()
cnx.close()
