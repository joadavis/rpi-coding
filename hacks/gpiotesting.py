# from www.thirdeyevis.com/pi-page-2.php

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)


def blinkity():
    for i in range(0,5):
        GPIO.output(13, True)
        time.sleep(.5)
        
        GPIO.output(7, True)
        time.sleep(.5)
        GPIO.output(7, False)
        time.sleep(.2)
        GPIO.output(11, True)
        time.sleep(.5)
        GPIO.output(11, False)
        time.sleep(.2)
        GPIO.output(11, True)
        time.sleep(.5)
        GPIO.output(11, False)
        time.sleep(.2)

        GPIO.output(13, False)
        time.sleep(.2)

def upity():
    for i in range(0,15):
        GPIO.output(13, True)
        time.sleep(.2)
        
        GPIO.output(7, True)
        time.sleep(.2)
        
        GPIO.output(11, True)
        time.sleep(.5)
        
        GPIO.output(11, False)
        GPIO.output(7, False)
        GPIO.output(13, False)
        time.sleep(.5)


#while True:
print("wait")
GPIO.wait_for_edge(12, GPIO.FALLING)
print("got")
blinkity()

GPIO.wait_for_edge(16, GPIO.FALLING)
upity()

GPIO.cleanup()
