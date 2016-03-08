# Simple blinking light program
# see makezine.com/projects/tutorial-raspberry-pi-gpio-pins-and-python/

import RPi.GPIO as GPIO
import time
import random

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD) # count pins from top left by board lights

GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)




def blinky(pinnum):
    for i in range(10):
        GPIO.output(pinnum, True)
        time.sleep(.3)
        GPIO.output(pinnum, False)
        time.sleep(.3)
    print "blinky Done"

def startup(pina, pinb, pinc, pind):
    GPIO.output(pina, True)
    time.sleep(1)
    GPIO.output(pinb, True)
    time.sleep(2)
    GPIO.output(pinc, True)
    time.sleep(3)
    GPIO.output(pind, True)
    time.sleep(4)
    GPIO.output(pina, False)
    GPIO.output(pinb, False)
    GPIO.output(pinc, False)
    GPIO.output(pind, False)
    time.sleep(.2)


def walky(pina, pinb, pinc, pind):
    for i in range(10):
        GPIO.output(pina, True)
        time.sleep(.2)

        GPIO.output(pinb, True)
        time.sleep(.2)

        GPIO.output(pina, False)
        GPIO.output(pinc, True)
        time.sleep(.2)

        GPIO.output(pinb, False)
        GPIO.output(pind, True)
        time.sleep(.2)

        GPIO.output(pinc, False)
        time.sleep(.2)

        GPIO.output(pind, False)
        time.sleep(.2)
    print "walky Done"


def walky3(pina, pinb, pinc, pind):
    for i in range(10):
        GPIO.output(pina, True)
        time.sleep(.1)

        GPIO.output(pinb, True)
        time.sleep(.1)

        
        GPIO.output(pinc, True)
        time.sleep(.1)

        GPIO.output(pina, False)
        
        GPIO.output(pind, True)
        time.sleep(.2)

        GPIO.output(pinb, False)
        time.sleep(.1)
        
        GPIO.output(pinc, False)
        time.sleep(.1)

        GPIO.output(pind, False)
        time.sleep(.1)
    print "walky3 Done"


def wavy(pina, pinb, pinc, pind):
    GPIO.output(pina, False)
    for i in range(10):
        wavetime = .2
        # make waves
        print "bump from b"
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
        print "bump from d"
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

    # on white
    GPIO.output(pina, True)
    time.sleep(2)
    GPIO.output(pina, False)
    print "wavy Done"


def stoplight(pina, pinb, pinc):
    pinaon = True
    pinbon = True
    pincon = True
    while True:
        randomswitch = random.randint(1,3)
        if randomswitch == 1:
            pinaon = not pinaon
        if randomswitch == 2:
            pinbon = not pinbon
        if randomswitch == 3:
            pincon = not pincon
        GPIO.output(pina, pinaon)
        GPIO.output(pinb, pinbon)
        GPIO.output(pinc, pincon)
        time.sleep(random.randint(1,3))
    print "oops"
 
def better_stoplight(pina, pinb, pinc):
    GPIO.output(pina, True)
    GPIO.output(pinb, True)
    GPIO.output(pinc, True)
    time.sleep(2)
    GPIO.output(pina, False)
    GPIO.output(pinb, False)
    GPIO.output(pinc, False)
    while True:
        GPIO.output(pina, False)
        GPIO.output(pinb, False)
        GPIO.output(pinc, True)
        time.sleep(random.randint(1,5))
        GPIO.output(pina, False)
        GPIO.output(pinb, True)
        GPIO.output(pinc, False)
        time.sleep(2)
        GPIO.output(pina, True)
        GPIO.output(pinb, False)
        GPIO.output(pinc, False)
        time.sleep(random.randint(2,5))

    



#startup(11,12,15,16)


#walky3(11,12,15,16)

#wavy(11, 12, 15, 16)

#blinky(11)

#blinky(11)




better_stoplight(11, 12, 15)





GPIO.cleanup()
