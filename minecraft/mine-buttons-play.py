# combo script

from mcpi import minecraft

import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

# convenience declares
dirt = 3
wool = 35
stone = 1
air = 0
tnt = 46
flower = 38



mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")



def makeflowers():
    # lets try making flowers
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, flower, 0)
    mc.setBlock(x, y, z+1, flower, 1)
    mc.setBlock(x-1, y, z, flower, 2)
    mc.setBlock(x, y, z-1, flower, 3)


def sine():
    x, y, z = mc.player.getPos()
    for sinus in range(1, 100):
        mc.setBlock(x + sinus, y + 4, z + math.sin(sinus), flower, 0)

def dosomething():
    sine()
    upity()



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


while True:
    GPIO.wait_for_edge(12, GPIO.FALLING)
    dosomething()
