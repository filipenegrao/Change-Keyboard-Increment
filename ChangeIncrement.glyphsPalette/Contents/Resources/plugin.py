# encoding: utf-8

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import GlyphsApp
from vanilla import *


class KeyboardIncrementClass(PalettePlugin):

    @objc.python_method
    def settings(self):

        self.value = 1
        self.name = 'Change Increment'

        # Create Vanilla window and group with controls
        width = 150
        height = 80
        self.paletteView = Window((width, height))
        self.paletteView.group = Group((0, 0, width, height))
        self.paletteView.group.plus = SquareButton((100, 15, -20, -45), "+", callback=self.incrementCallback_)
        self.paletteView.group.minus = SquareButton((20, 15, -100, -45), "-", callback=self.decrementCallback_)
        self.paletteView.group.txt = EditText((70, 15, -70, -45), text=self.value, sizeStyle='small', callback=self.textCallback_)
        self.paletteView.group.resetButton = SquareButton((20, 45, -20, -15), "reset to default", sizeStyle='mini', callback=self.resetDefaults_)

        # shortcuts
        self.paletteView.group.plus.bind("uparrow", ["command"])
        self.paletteView.group.minus.bind("downarrow", ["command"])
        self.paletteView.group.resetButton.bind("forwarddelete",["command"])

        # Set dialog to NSView
        self.dialog = self.paletteView.group.getNSView()

    @objc.python_method
    def start(self):
        # Adding a callback for the 'GSUpdateInterface' event
        Glyphs.addCallback(self.update_, UPDATEINTERFACE)

    @objc.python_method
    def __del__(self):
        Glyphs.removeCallback(self.update)

    def update_(self, sender):
        self.font = sender.object()

    def incrementCallback_(self, sender):
        self.value += 1
        self.paletteView.group.txt.set(self.value)
        self.newValue()
        self.setIncrement()

    def decrementCallback_(self, sender):
        self.value -= 1
        self.paletteView.group.txt.set(self.value)
        self.newValue()
        self.setIncrement()

    def textCallback_(self, sender):
        self.newValue()
        self.setIncrement()

    @objc.python_method
    def newValue(self):
        n = self.paletteView.group.txt.get()
        return int(n)

    @objc.python_method
    def setIncrement(self):
        # Kerning increments:
        Glyphs.intDefaults["GSKerningIncrementLow"] = self.newValue()
        Glyphs.intDefaults["GSKerningIncrementHigh"] = self.newValue() * 10

        # Spacing increments:
        Glyphs.intDefaults["GSSpacingIncrementLow"] = self.newValue()
        Glyphs.intDefaults["GSSpacingIncrementHigh"] = self.newValue() * 10

        self.font.keyboardIncrement = float(self.newValue())

    def resetDefaults_(self, sender):
        self.value = 1
        self.paletteView.group.txt.set(self.value)
        self.newValue()
        self.setIncrement()
        # self.paletteView.group.txt.set(self.value)
        # del(Glyphs.intDefaults["GSSpacingIncrementLow"])
        # del(Glyphs.intDefaults["GSSpacingIncrementHigh"])

    @objc.python_method
    def __file__(self):
        """Please leave this method unchanged"""
        return __file__
