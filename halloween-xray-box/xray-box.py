# xray box simulator
# flash some lights at the push of a button

# joadavis 23Oct2015

# I used this script by taking advice from
# http://embeddedday.com/projects/raspberry-pi/a-step-further/running-python-script-at-boot/
# and using "sudo crontab -e" to specify a path to this file.
# Then I ran my pi headless from a usb battery pack and it started automatically.
# With the one button wired up, I  was able to flash a set of LEDs attached to pins below.


import RPi.GPIO as GPIO
import time

# todo import random and random patterns

pinb = 10
pinc = 11
pind = 15
pinw = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def doScan(channel):
    print("Starting scan")

    GPIO.output(pinb, False)
    GPIO.output(pinc, False)
    GPIO.output(pind, False)
    GPIO.output(pinw, False)
    
    # make waves
    for i in range(3):
        wavetime = .1
        # make waves
        #print "bump from b"
        GPIO.output(pinb, True)
        time.sleep(wavetime)
        
        GPIO.output(pinc, True)
        time.sleep(wavetime)
        
        GPIO.output(pind, True)
        time.sleep(wavetime)

        GPIO.output(pind, False)
        time.sleep(wavetime)
        
        GPIO.output(pinc, False)
        time.sleep(wavetime)

        GPIO.output(pinb, False)
        time.sleep(wavetime)

        #
        GPIO.output(pinb, True)
        time.sleep(wavetime)
        
        GPIO.output(pinc, True)
        time.sleep(wavetime)
        
        GPIO.output(pind, True)
        GPIO.output(pinb, False)
        time.sleep(wavetime)

        GPIO.output(pinc, False)
        time.sleep(wavetime)

        GPIO.output(pind, False)
        time.sleep(wavetime)

        #
        #print "bump from d"
        GPIO.output(pind, True)
        time.sleep(wavetime)
        
        GPIO.output(pinc, True)
        time.sleep(wavetime)

        GPIO.output(pinb, True)
        time.sleep(wavetime)

        GPIO.output(pinb, False)
        time.sleep(wavetime)

        GPIO.output(pinc, False)
        time.sleep(wavetime)

        GPIO.output(pind, False)
        time.sleep(wavetime)

        #
        GPIO.output(pind, True)
        time.sleep(wavetime)
        
        GPIO.output(pinc, True)
        time.sleep(wavetime)

        GPIO.output(pinb, True)
        GPIO.output(pind, False)
        time.sleep(wavetime)

        GPIO.output(pinc, False)
        time.sleep(wavetime)

        GPIO.output(pinb, False)
        time.sleep(wavetime)

    GPIO.output(pinb, False)
    GPIO.output(pinc, False)
    GPIO.output(pind, False)

    print("display")
    GPIO.output(pinw, True)
    time.sleep(10)
    GPIO.output(pinw, False)
    
    print("Scan complete")


def doScanBuildup(channel):
    print("Starting scan b")

    GPIO.output(pinb, False)
    GPIO.output(pinc, False)
    GPIO.output(pind, False)
    GPIO.output(pinw, False)
    
    # make waves
    wavetime = .3
    for i in range(5):
        wavetime = wavetime - 0.05
        # make waves
        #print "bump from b"
        GPIO.output(pinb, True)
        time.sleep(wavetime)
        
        GPIO.output(pinc, True)
        time.sleep(wavetime)

        GPIO.output(pinb, False)
        GPIO.output(pind, True)
        time.sleep(wavetime)
        
        GPIO.output(pinc, False)
        time.sleep(wavetime)

        GPIO.output(pind, False)
        time.sleep(wavetime)


    GPIO.output(pinb, False)
    GPIO.output(pinc, False)
    GPIO.output(pind, False)

    print("display b")
    GPIO.output(pinw, True)
    time.sleep(10)
    GPIO.output(pinw, False)
    
    print("Scan complete b")



GPIO.add_event_detect(38, GPIO.RISING, callback=doScanBuildup, bouncetime=3000)


while True:
    GPIO.wait_for_edge(37, GPIO.FALLING)
    print("how'd that happen?")
    doScan()

# wont ever get here in this version
GPIO.cleanup()
