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

stdscr.addstr(1,1, "+--------+")

# use BCM GPIO refs
GPIO.setmode(GPIO.BCM)



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
     stdscr.addstr(2, 5, 'Run')  


  def setup(self):
    for pin in self.pins:
      stdscr.addstr(2, 16, "setup pin %i" % pin)
      GPIO.setup(pin, GPIO.OUT)
      GPIO.output(pin, False)

  #def zero_counter(self):

stdscr.addstr(10, 1, "Init motors")
#motor_left = Motor([17, 18, 22, 23])
#motor_right = Motor([19, 6, 16, 12]) 
#motor_right.stepratio = 9
motor_1 = Motor([17, 18, 22, 23])
motor_2 = Motor([19, 6, 16, 12])
motor_3 = Motor([9, 11, 8, 7])


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




# help text
stdscr.addstr(4,1, "stepper mover controls")
stdscr.addstr(5,1, "q  - quit")
stdscr.addstr(6,1, "e and d - motor 1")
stdscr.addstr(7,1, "t and g - motor 2")
stdscr.addstr(8,1, "u and j - motor 3")
stdscr.addstr(9,1, "o and l - motor 4")

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

  elif key == ord('e'):
    motor_1.run(1, 1)
  elif key == ord('d'):
    motor_1.run(1, -1)
    
  elif key == ord('t'):
    motor_2.run(1, 1)
  elif key == ord('g'):
    motor_2.run(1, -1)

  elif key == ord('u'):
    motor_3.run(1, 1)
  elif key == ord('j'):
    motor_3.run(1, -1)
    
  #elif key == ord('o'):
  #  motor_4.run(1, 1)
  #elif key == ord('l'):
  #  motor_4.run(1, -1)

  

GPIO.cleanup()
curses.endwin()

