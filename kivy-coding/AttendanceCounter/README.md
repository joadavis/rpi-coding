# AttendanceCounter

A simple hand-held app to count attendance in a room.


## Design and Description

I designed AttendanceCounter to help me know how many people were attending Sacrament
meeting at church.  Without it, I would make notes on paper.  Usually I would count
how many people were in each row and write the row count in a spacial area to help
keep track, sometimes with a name next to it to help if I lost my place.  Then after
the meeting I'd add up all the numbers and double check.

With the app, I wanted something I could just tap to count up heads, but also have
that spacial sense to make it easier to keep track of which rows I'd already done.
Being able to subtract and adjust counts was also critical, as in a large room people
move around.

I designed it to load up the room layout from a configuration so it could be adjusted
to the venue.

I wrote it to be used on my Samsung Galaxy S4 (using qPython back when it worked), but
it works fine on other Kivy environments.

### Room Design

The types of seating in the original version are:

* LongBench (up to 20)
* MediumBench (up to 12)
* Chair (up to 2)
* Spacer (no seats)

Each type of seating has a class defined in main.py that defines its maximum allowed
number of people, to avoid holding ridiculous values.

The look of each type of seating is defined in attendancecounter.kv, so if a new type
of seating is desired it will also need to be defined there.

In addition to seating, the room can be broken up into areas (stage, main, overflow)
and separated (curtain or podium).

The intent was to allow reading in the room design from a config, but in the original
version it is just loaded from the build() method.


# Enjoy -joadavis

Copyright (c) 2015-2018 Joseph Davis

Licensed under the MIT license, as is the other code in this github repo
