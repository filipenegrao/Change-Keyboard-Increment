# encoding: utf-8

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import GlyphsApp
from vanilla import *


class KeyboardIncrementClass(PalettePlugin):

    def settings(self):

        self.value = 1
        self.name = 'Change Increment'

        # Create Vanilla window and group with controls
        width = 150
        height = 80
        self.paletteView = Window((width, height))
        self.paletteView.group = Group((0, 0, width, height))
        self.paletteView.group.plus = SquareButton((100, 15, -20, -45), "+", callback=self.incrementCallback)
        self.paletteView.group.minus = SquareButton((20, 15, -100, -45), "-", callback=self.decrementCallback)
        self.paletteView.group.txt = EditText((70, 15, -70, -45), text=self.value, sizeStyle='small', callback=self.textCallback)
        self.paletteView.group.resetButton = SquareButton((20, 45, -20, -15), "reset to default", sizeStyle='mini', callback=self.resetDefaults)

        # shortcuts
        self.paletteView.group.plus.bind("uparrow", ["command"])
        self.paletteView.group.minus.bind("downarrow", ["command"])
        self.paletteView.group.resetButton.bind("forwarddelete",["command"])

        # Set dialog to NSView
        self.dialog = self.paletteView.group.getNSView()

    def start(self):
        # Adding a callback for the 'GSUpdateInterface' event
        Glyphs.addCallback(self.update, UPDATEINTERFACE)

    def __del__(self):
        Glyphs.removeCallback(self.update)

    def update(self, sender):
        self.font = sender.object()

    def incrementCallback(self, sender):
        self.value += 1
        self.paletteView.group.txt.set(self.value)
        self.newValue()
        self.setIncrement()

    def decrementCallback(self, sender):
        self.value -= 1
        self.paletteView.group.txt.set(self.value)
        self.newValue()
        self.setIncrement()

    def textCallback(self, sender):
        self.newValue()
        self.setIncrement()

    def newValue(self):
        n = self.paletteView.group.txt.get()
        return int(n)

    def setIncrement(self):
        # Kerning increments:
        Glyphs.intDefaults["GSKerningIncrementLow"] = self.newValue()
        Glyphs.intDefaults["GSKerningIncrementHigh"] = self.newValue() * 10

        # Spacing increments:
        Glyphs.intDefaults["GSSpacingIncrementLow"] = self.newValue()
        Glyphs.intDefaults["GSSpacingIncrementHigh"] = self.newValue() * 10

        self.font.keyboardIncrement = float(self.newValue())

    def resetDefaults(self, sender):
        self.value = 1
        self.paletteView.group.txt.set(self.value)
        self.newValue()
        self.setIncrement()
        # self.paletteView.group.txt.set(self.value)
        # del(Glyphs.intDefaults["GSSpacingIncrementLow"])
        # del(Glyphs.intDefaults["GSSpacingIncrementHigh"])

    def __file__(self):
        """Please leave this method unchanged"""
        return __file__

    # Temporary Fix
    # Sort ID for compatibility with v919:
    _sortID = 0
    def setSortID_(self, id):
        try:
            self._sortID = id
        except Exception as e:
            self.logToConsole( "setSortID_: %s" % str(e) )
    def sortID(self):
        return self._sortID
