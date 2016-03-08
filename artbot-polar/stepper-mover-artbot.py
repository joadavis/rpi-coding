#!/usr/bin/python
# from raspberrypi-spy.co.uk
# and a reference for curses

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
#StepPins = [19, 16, 26, 20]   # GPIO numbering

# motor 1
StepPins = [17, 18, 22, 23]   # GPIO numbering
#StepPins = [18, 17, 22, 23]   # GPIO numbering


# motor 2
StepPins = [19, 6, 16, 12]



class Motor:
  stepratio = 1
  pins = []
  dir_flip = 1
  wind_count = 0
  step_counter = 0
  def __init__(self, somepins, someratio=1):
    self.pins = somepins
    self.stepratio = someratio
    self.setup()
    
  def run(self, relsteps=5, direction=1):
     # turn the spool a relative amount
     my_steps = relsteps * self.stepratio
     my_dir = direction * self.dir_flip
     # todo loop to step through sequence
     for loops in range(my_steps):
       #print("counting ",)
       #print(self.step_counter,)
       #print(Seq[self.step_counter])
       stdscr.addstr(2, 12, str(self.step_counter))
       stdscr.addstr(2, 14, str(Seq[self.step_counter]))

       for pin in range(0,4):
         xpin = self.pins[pin]
         if Seq[self.step_counter][pin] != 0:
           #print(" enable GPIO %i" % (xpin))
           stdscr.addstr(2, 8, str(xpin))
           GPIO.output(xpin, True)
         else:
           GPIO.output(xpin, False)

       self.step_counter += my_dir

       # if end, start again
       if (self.step_counter >= StepCountMax):
         self.step_counter = 0
       if (self.step_counter < 0):
         self.step_counter = StepCountMax + my_dir

       time.sleep(WaitTime)
     #print("o")
     stdscr.addch(2, 5, 'R')  


  def setup(self):
    for pin in self.pins:
      print("setup pin %i" % pin)
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, False)

  #def zero_counter(self):

print("Init motors")
motor_left = Motor([17, 18, 22, 23])
motor_right = Motor([19, 6, 16, 12]) 
motor_right.stepratio = 9


# set all pins as ouput
#for pin in StepPins:
#  print("Setup pins")
#  GPIO.setup(pin, GPIO.OUT)
#  GPIO.output(pin, False)

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

#Seq = FullSeq

StepCountMax = len(Seq)
StepDir = 1 # positive clockwise, negative counterclockwise
wind = 1
unwind = -1

# read wait time from command line
if len(sys.argv) > 1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# init
#StepCounter = 0


def write_hi():
  motor_right.run(100, 1)
  motor_right.run(50, -1)
  motor_left.run(80, -1)
  motor_right.run(50, -1)
  motor_right.run(100, 1)

  motor_left.run(80, -1)

  motor_right.run(50, -1)
  motor_left.run(20, -1)
  motor_right.run(20, -1)
  motor_left.run(20, 1)
  motor_right.run(20, 1)


def write_box():
  motor_right.run(500, 1)
  motor_left.run(500, 1)
  motor_right.run(500, -1)
  motor_left.run(500, -1)
  #print("Boxed")


def write_star():
  line_down()
  line_down()
  line_down()
  line_left()
  line_down()
  line_down()
  line_down()
  line_left()
  line_down()
  line_down()
  line_down()
  line_right()
  line_up()
  line_right()
  line_up()
  line_right()
  line_up()
  line_right()
  line_up()
  line_right()
  line_up()
  line_right()
  line_up()
  line_left()
  line_left()
  line_left()
  line_left()
  line_left()
  line_left()
  line_left()
  line_left()
  line_left()
  line_down()
  line_right()
  line_down()
  line_right()
  line_down()
  line_right()
  line_down()
  line_right()
  line_down()
  line_right()
  line_down()
  line_right()
  line_up()
  line_up()
  line_up()
  line_left()
  line_up()
  line_up()
  line_up()
  line_left()
  line_up()
  line_up()
  line_up()
  line_left()
  pass


def line_left():
  for x in range(10):
    motor_right.run(1, -1)
    motor_left.run(1, 1)

def line_right():
  for x in range(10):
    motor_right.run(1, 1)
    motor_left.run(1, -1)

def line_up():
  for x in range(10):
    motor_right.run(1, 1)
    motor_left.run(1, 1)

def line_down():
  for x in range(10):
    motor_right.run(1, -1)
    motor_left.run(1, -1)


def write_fill():
  for lef in range(20):
    for rig in range(100):
      motor_right.run(1,1)
    motor_left.run(2,-1)
    for rig in range(100):
      motor_right.run(1, -1)
    motor_left.run(2,-1)


def write_linestars():
  for linlen in range(8):
    write_star()
    for moveright in range(10):
      line_right()


# help text
stdscr.addstr(4,1, "art bot controls")
stdscr.addstr(5,1, "q  - quit")
stdscr.addstr(6,1, "w and s - left motor wind/unwind")
stdscr.addstr(7,1, "i and k - right motor wind/unwind")
stdscr.addstr(8,1, "t - line up")
stdscr.addstr(9,1, "g - line down")
stdscr.addstr(10,1, "f - line left")
stdscr.addstr(11,1, "h - line right")
stdscr.addstr(12,1, "1 to 4 - presets")
stdscr.addstr(13,1, "5 - write a line of stars, start on the far left")

# main loop
#while True:
key = ''
while key != ord('q'):
  key = stdscr.getch()
  #stdscr.addch(2, 5, key)
  #stdscr.refresh()
  if key == curses.KEY_UP:
    StepDir = 1
  elif key == curses.KEY_DOWN:
    StepDir = -1

  elif key == ord('w'):
    motor_left.run(1, 1)
  elif key == ord('s'):
    motor_left.run(1, -1)
  elif key == ord('i'):
    motor_right.run(1, 1)
  elif key == ord('k'):
    motor_right.run(1, -1)

  elif key == ord('t'):
    line_up()
  elif key == ord('g'):
    line_down()

  elif key == ord('h'):
    line_right()
  elif key == ord('f'):
    line_left()

  # some preprogrammed moves
  elif key == ord('1'):
    write_hi()
  elif key == ord('2'):
    write_box()
  elif key == ord('3'):
    write_star()
  elif key == ord('4'):
    write_fill()
  elif key == ord('5'):
    write_linestars()


GPIO.cleanup()
curses.endwin()

