#!/usr/bin/python
# from raspberrypi-spy.co.uk


import sys
import time
import RPi.GPIO as GPIO

import curses
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

# use BCM GPIO refs
GPIO.setmode(GPIO.BCM)

# define pins
#StepPins = [17, 22, 23, 24]
#StepPins = [35, 36, 37, 38]  # order on board
#StepPins = [19, 16, 26, 20]

# motor 2
StepPins = [19, 6, 16, 12]

# motor 1
#StepPins = [17, 18, 22, 23]   # GPIO numbering
#StepPins = [18, 17, 22, 23]   # GPIO numbering


# set all pins as ouput
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, False)

#define sequence for halfstepping
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]
# full stepping
FullSeq = [[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]]

Seq = FullSeq

StepCount = len(Seq)
StepDir = 1 # positive clockwise, negative counterclockwise

# read wait time from command line
if len(sys.argv) > 1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# init
StepCounter = 0

# main loop
#while True:

key = ''
while key != ord('q'):
  key = stdscr.getch()
  stdscr.addch(2, 25, key)
  stdscr.refresh()
  if key == curses.KEY_UP:
    StepDir = 1
  elif key == curses.KEY_DOWN:
    StepDir = -1
  
  print "counting ",
  print StepCounter,
  print Seq[StepCounter]

  for pin in range(0,4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin] != 0:
      print " enable GPIO %i" % (xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir

  # if end, start again
  if (StepCounter >= StepCount):
    StepCounter = 0
  if (StepCounter < 0):
    StepCounter = StepCount + StepDir

  time.sleep(WaitTime)

GPIO.cleanup()
curses.endwin()
