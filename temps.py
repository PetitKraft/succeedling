#coding: utf-8

import mysql.connector
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time



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
inside_temp = inside_sensor.get_temperature()
outside_temp = outside_sensor.get_temperature()



# 気温に基づいてサイドビニールの開け閉め
#if inside_temperature =    
#    GPIO.output(lwin_lpwm, isUp)
#    GPIO.output(lwin_rpwm, not(isUp))
#    GPIO.output(rwin_lpwm, not(isUp))
#    GPIO.output(rwin_rpwm, isUp)



# DBへの挿入
data = {
    "inside_temp": inside_temp,
    "outside_temp": outside_temp,
}
cursor.execute(register_temps, data)



cursor.close()
cnx.commit()
cnx.close()
