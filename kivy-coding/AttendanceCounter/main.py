#-*-coding:utf8;-*-
#qpy:2
#qpy:kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, Ellipse, Line
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
import os
from datetime import datetime


class ChapelMap(BoxLayout):
    num_adj = 1
    all_total = 0
    total_label_ref = None

    def __init__(self, **kwargs):
        super(ChapelMap, self).__init__(**kwargs)
        self.orientation = 'vertical'

    def calculate_total(self):
        sum_total = 0
        for area in self.children:
            for kid in area.children:
                #sum_total += 1
                if kid.text.isdigit():
                    sum_total += int(kid.text)
        all_total = sum_total
        print "Total is " + str(all_total)
        self.total_label_ref.text = "Total = " + str(sum_total)


class RowInput(Widget):
    pass


class ChapelArea(GridLayout):
    pass


# area for display of current value and controls
class InputArea(BoxLayout):
    pass


class Spacer(Button):
    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.size_hint = (.5, .5)
        #self.background_color = (.1, .1, .1, .3)
        self.background_color = (.1, .1, .6, 1)


class Chair(Button):
    def on_press(self):
        num = int(self.text)
        #num += 1
        num += self.parent.parent.num_adj
        if num > 2:
            # should spit out a warning
            num = 2
        elif num < 0:
            num = 0
        self.text = str(num)
        self.parent.parent.calculate_total()

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.size_hint = (.5, .8)
        self.text = "0"
        #self.background_color = (.38, .38, .38, 1)
        self.background_color = (.45, .45, .45, 1)


class MediumBench(Button):
    def on_press(self):
        num = int(self.text)
        #num += 1
        num += self.parent.parent.num_adj
        if num > 12:
            num = 12
        elif num < 0:
            num = 0
        self.text = str(num)
        self.parent.parent.calculate_total()
        #with self.canvas:
        #    Color(.8, .8, .5, .5)
        #    print str(self.center_x) + " " + str(self.x) + " " + str(self.width)
        #    Line(points=[self.x+1, self.y+2, self.x + self.width - 1, self.y + 2])

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        self.size_hint = (.7, 1)
        self.text = "0"
        self.background_color = (.45, .06, .2, 1)
        # experimenting
        #self.border = (16, 32, 16, 32)
        #self.padding = (4, 4)
        #with self.canvas:
        #    Color(1, 1, 0)
        #    d = 30.
        #    print str(self.center_x) + " " + str(self.x) + " " + str(self.width)  # this is returning junk
        #    Ellipse(pos=(self.x - d / 2, self.y - d / 2), size=(d, d))


class LongBench(Button):
    def on_press(self):
        num = int(self.text)
        #num += 1
        num += self.parent.parent.num_adj
        if num > 20:
            num = 20
        elif num < 0:
            num = 0
        self.text = str(num)
        self.parent.parent.calculate_total()

    def __init__(self, **kwargs):
        super(Button, self).__init__(**kwargs)
        #self.size_hint = (1.2, .9)
        self.text = "0"
        #self.background_color = (.45, .06, .2, 1)
        self.background_color = (.55, .16, .3, 1)


def add_seats(seat_list, parent_widg):
    for seat in seat_list:
        if seat == "chair":
            parent_widg.add_widget(Chair())
        elif seat == "med":
            parent_widg.add_widget(MediumBench())
        elif seat == "long":
            parent_widg.add_widget(LongBench())
        else:
            parent_widg.add_widget(Spacer())


def invert_action(self):
    new_num = self.parent.parent.num_adj * -1
    self.parent.parent.num_adj = new_num
    if new_num > 0:
        self.text = "Adding"
    else:
        self.text = "Subtracting"


def save_action(self):
    # save the total out to a file, with a timestamp
    # note that the label is of the form "Total = 3"
    print os.getcwd()
    print self.total_label_ref.text
    # TODO need a file chooser
    #with open("C:\\Temp\\attendancecountertotals.txt", "a+") as f:
    with open("attendancecountertotals.txt", "a+") as f:  # unfortunately, this goes into the kivy folder
        f.write(str(datetime.now()) + "\t")
        f.write(self.total_label_ref.text + "\n")


class AttendancecounterApp(App):
    #rowlist = "chair, med, med, med, med, colbreak, chair, med, med, med, med, fullbreak, 10 med, 10 long, 10 med, fullbreak, long, long, long, colbreak, long, long, long"
    # or just use an array, or take a string and split it into an array
    # or write a method that takes a list and has an if case that adds them to the widget in order
    # if we are using GridLayout widgets, it is just the order that matters
    # and generate a unique id for each new widget, and put the unique ids into an array for later...
    # or just use the widget

    def build(self):
        #parent = Widget()

        chapel = ChapelMap(size_hint=(1, 1.5))  # so it will scroll

        stage = ChapelArea(cols=4, size_hint=(1, .3), spacing=8)
        add_seats(["chair", "long", "long", "chair",
                   # "spacer", "long", "long", "spacer",
                   "spacer", "long", "long", "spacer",
                   "spacer", "long", "long", "spacer",
                   "med", "long", "long", "med"], stage)

        main_area = ChapelArea(cols=3, spacing=8)
        # by rows
        add_seats(["med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "med", "long", "med",
                   "chair", "spacer", "chair"], main_area)

        # overflow is only 3 rows, so hint it shorter
        overflow = ChapelArea(cols=4, size_hint=(1, .25), spacing=8)
        add_seats(["med", "long", "long", "med",
                   "spacer", "long", "long", "spacer",
                   "spacer", "long", "long", "spacer"], overflow)

        podium = Label(text="podium", 
        	#text_size=(None, 24), 
        	#font_size=24,
        	size_hint=(1, .1)
        	)
        chapel.add_widget(stage)
        chapel.add_widget(podium)
        chapel.add_widget(main_area)
        curtain = Label(text="curtain", 
        	#text_size=(None, 10), 
        	#font_size=8,
        	size_hint=(1, .1)
        	)
        chapel.add_widget(curtain)
        chapel.add_widget(overflow)

        #total_bar = BoxLayout(background_color=(.8, .8, .8, 1), size_hint=(1, .15))
        total_bar = InputArea(background_color=(.8, .8, .8, 1), size_hint=(1, .15))
        total = Label(text="Total = " + str(chapel.all_total))
        #total.bind(text="Total = " + str(chapel.all_total))
        chapel.total_label_ref = total
        invert_button = ToggleButton(text='Adding')
        invert_button.bind(on_press=invert_action)
        save_button = Button(text='Save')
        save_button.bind(on_press=save_action)
        save_button.total_label_ref = total
        total_bar.add_widget(total)
        total_bar.add_widget(invert_button)
        total_bar.add_widget(save_button)
        chapel.add_widget(total_bar)
        #return chapel

        scroller = ScrollView() # size_hint=(None, None))  # , size=(400, 400))
        scroller.add_widget(chapel)
        return scroller

    def on_pause(self):
        print "pausing " #at %s" % all_total
        return True
    
    def on_resume(self):
        print "resuming " #at %s" % all_total
        pass


if __name__ == '__main__':
    AttendancecounterApp().run()