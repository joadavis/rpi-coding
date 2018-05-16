#qpy:kivy
'''
what started as a Pictures demo
Coerced into Roll and Tell - JAD
=============

This is a basic picture viewer, using the scatter widget.
'''

import kivy
kivy.require('1.0.6')

from glob import glob
from random import randint
from os.path import join, dirname
from kivy.app import App
from kivy.logger import Logger
from kivy.uix.scatter import Scatter
from kivy.properties import StringProperty
# FIXME this shouldn't be necessary
from kivy.core.window import Window
import time


class Picture(Scatter):
    '''Picture is the class that will show the image with a white border and a
    shadow. They are nothing here because almost everything is inside the
    picture.kv. Check the rule named <Picture> inside the file, and you'll see
    how the Picture() is really constructed and used.

    The source property will be the filename to show.
    '''

    source = StringProperty(None)


class PicturesApp(App):

    all_images = []
    selected_images = set()
    select_this_many = 9

    def get_all_tiles(self, tiledir):
        print "getting tiles"
        scatter_area_x = Window.width
        scatter_area_y = Window.height
        for filename in glob(tiledir):
            print filename
            try:
                picture = Picture(source=filename, rotation=randint(-30, 30))  #-60, 60))
                picture.pos = (randint(picture.width, scatter_area_x - picture.width * 2), randint(picture.height, scatter_area_y/2 - picture.height))
                self.all_images.append(picture)
            except Exception, e:
                Logger.exception('RollAndTell: Unable to load <%s>' % filename)


    def select_some_tiles(self):
        print "picky picky"
        scatter_area_x = Window.width
        scatter_area_y = Window.height
        if (len(self.all_images) <= self.select_this_many):
            self.selected_images = set(self.all_images)
            return
        self.selected_images = set()
        while len(self.selected_images) < self.select_this_many:
            print "maybe another"
            ind = randint(0, len(self.all_images)-1)
            picture = self.all_images[ind]
            picture.scale = 4.8 #1.2
            picture.pos = (randint(picture.width, scatter_area_x - picture.width * 2), randint(picture.height, scatter_area_y/2 - picture.height))
            self.selected_images.add(self.all_images[ind])




    '''
    def build(self):

        # the root is created in pictures.kv
        root = self.root

        # get any files into images directory
        curdir = dirname(__file__)
        #for filename in glob(join(curdir, 'images', '*')):
        for filename in glob(join(curdir, '../../icontiles', '*')):
            # TODO: only pick 9 of the tiles, but load all tiles into an image array
            try:
                # load the image
                picture = Picture(source=filename, rotation=randint(-45,45))
                # TODO: random position of the pictures in bottom half of area
                # add to the main field
                root.add_widget(picture)
            except Exception, e:
                Logger.exception('Pictures: Unable to load <%s>' % filename)
    '''

    def build(self):
        root = self.root

        # create buttons
        root.save_butt.bind(on_release=self.save_snapshot)
        root.roll_butt.bind(on_release=self.roll_tiles)


        curdir = dirname(__file__)
        tiledir = join(curdir, './icontiles', '*')
        print tiledir
        self.get_all_tiles(tiledir)

        #for imtile in self.all_images:
        #    root.add_widget(imtile)

        self.select_some_tiles()
        for imtile in self.selected_images:
            root.add_widget(imtile)



    def on_pause(self):
        return True


    def save_snapshot(self, something):
        #print something
        global Screenshotnum
        filename = "RollAndTell-%s.png" % time.time()
        Window.screenshot(name=filename)


    def roll_tiles(self, rolledbutton):
        root = self.root

        print root.ids
        # clear play area
        print "clearing"

        for child in root.children[:]:
            #print "id: %s" % child.id
            #print child.cls
            print child.width
            # use a little expert knowledge of what is in the .kv file
            if child.width == 52:
                root.remove_widget(child)
        #root.clear_widgets() # also removes buttons and label...

        # re-select tiles
        self.select_some_tiles()

        # reinsert tiles in play area
        for imtile in self.selected_images:
            # TODO: reposition tiles also
            root.add_widget(imtile)


if __name__ == '__main__':
    PicturesApp().run()

