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



def dosomething():
    # lets try making flowers
    x, y, z = mc.player.getPos()
    mc.setBlock(x+1, y, z, flower, 0)
    mc.setBlock(x, y, z+1, flower, 1)
    mc.setBlock(x-1, y, z, flower, 2)
    mc.setBlock(x, y, z-1, flower, 3)



while True:
    GPIO.wait_for_edge(12, GPIO.FALLING)
    dosomething()
