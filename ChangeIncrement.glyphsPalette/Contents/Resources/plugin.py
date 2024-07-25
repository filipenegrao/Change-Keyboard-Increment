# encoding: utf-8

###########################################################################################################
#
#
#  Palette Plugin
#
#  Read the docs:
#  https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Palette
#
#
###########################################################################################################

from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import Glyphs
from GlyphsApp.plugins import PalettePlugin
import platform


class KeyboardIncrement(PalettePlugin):

	# the view
	dialog = objc.IBOutlet()

	# keyboard increment changer UIs
	keyboard_switch = objc.IBOutlet()
	keyboard_txt_keys = objc.IBOutlet()
	keyboard_txt_shift = objc.IBOutlet()

	# metrics increment changer UIs
	metrics_switch = objc.IBOutlet()
	metrics_txt_keys = objc.IBOutlet()
	metrics_txt_shift = objc.IBOutlet()

	# kerning increment changer UIs
	kerning_switch = objc.IBOutlet()
	kerning_txt_keys = objc.IBOutlet()
	kerning_txt_shift = objc.IBOutlet()

	@objc.python_method
	def settings(self):
		self.name = Glyphs.localize({
			'en': 'Keyboard Increment',
			# 'de': 'Meine Palette',
			# 'fr': 'Ma palette',
			# 'es': 'Mi panel',
			'pt': 'Incremento de Teclado',
		})

		# Load .nib dialog (without .extension)
		versionStr = platform.mac_ver()[0]
		parts = versionStr.split(".")
		if float(parts[0] + "." + parts[1]) >= 10.15:
			self.loadNib('IBdialog', __file__)
		else:
			self.loadNib('IBdialogpre15', __file__)

	@objc.python_method
	def start(self):
		Glyphs.registerDefault('com.filipenegrao.Increment.keyboard_small', 1)
		Glyphs.registerDefault('com.filipenegrao.Increment.keyboard_big', 10)

		Glyphs.registerDefault('com.filipenegrao.Increment.metrics_small', 1)
		Glyphs.registerDefault('com.filipenegrao.Increment.metrics_big', 10)

		Glyphs.registerDefault('com.filipenegrao.Increment.kerning_small', 1)
		Glyphs.registerDefault('com.filipenegrao.Increment.kerning_big', 10)

		Glyphs.registerDefault('com.filipenegrao.Increment.keyboard', False)
		Glyphs.registerDefault('com.filipenegrao.Increment.metrics', False)
		Glyphs.registerDefault('com.filipenegrao.Increment.kerning', False)

		self.keyboard_txt_keys.setIntValue_(Glyphs.defaults['com.filipenegrao.Increment.keyboard_small'])
		self.keyboard_txt_shift.setIntValue_(Glyphs.defaults['com.filipenegrao.Increment.keyboard_big'])

		self.metrics_txt_keys.setIntValue_(Glyphs.defaults['com.filipenegrao.Increment.metrics_small'])
		self.metrics_txt_shift.setIntValue_(Glyphs.defaults['com.filipenegrao.Increment.metrics_big'])

		self.kerning_txt_keys.setIntValue_(Glyphs.defaults['com.filipenegrao.Increment.kerning_small'])
		self.kerning_txt_shift.setIntValue_(Glyphs.defaults['com.filipenegrao.Increment.kerning_big'])

		self.keyboard_switch.setObjectValue_(bool(Glyphs.defaults['com.filipenegrao.Increment.keyboard']))
		self.metrics_switch.setObjectValue_(bool(Glyphs.defaults['com.filipenegrao.Increment.metrics']))
		self.kerning_switch.setObjectValue_(bool(Glyphs.defaults['com.filipenegrao.Increment.kerning']))

		# if Glyphs.versionNumber <= 3.0:
		# 	self.keyboard_txt_shift.isEditable = False

	@objc.IBAction
	def setKeyboardSmall_(self, sender):
		key_small = sender.intValue()
		Glyphs.defaults['com.filipenegrao.Increment.keyboard_small'] = key_small
		self.keyboard_txt_keys.setIntValue_(key_small)

	@objc.IBAction
	def setKeyboardBig_(self, sender):
		key_big = sender.intValue()
		Glyphs.defaults['com.filipenegrao.Increment.keyboard_big'] = key_big
		self.keyboard_txt_shift.setIntValue_(key_big)

	@objc.IBAction
	def applyKeyboard_(self, sender):
		switch_on = bool(sender.objectValue())
		font = Glyphs.font

		if switch_on:
			try:
				# Glyphs 3
				font.keyboardIncrement = Glyphs.defaults['com.filipenegrao.Increment.keyboard_small']
				font.keyboardIncrementBig = Glyphs.defaults['com.filipenegrao.Increment.keyboard_big']
			except:
				# Glyphs 2
				keyboardIncrement = Glyphs.defaults['com.filipenegrao.Increment.keyboard_small']

		else:
			try:
				# Glyphs 3
				font.keyboardIncrement = 1
				font.keyboardIncrementBig = 10
			except:
				# Glyphs 2
				font.keyboardIncrement = 1

	@objc.IBAction
	def setMetricsSmall_(self, sender):
		metrics_small = sender.intValue()
		Glyphs.defaults['com.filipenegrao.Increment.metrics_small'] = metrics_small
		self.metrics_txt_keys.setIntValue_(metrics_small)

	@objc.IBAction
	def setMetricsBig_(self, sender):
		metrics_big = sender.intValue()
		Glyphs.defaults['com.filipenegrao.Increment.metrics_big'] = metrics_big
		self.metrics_txt_shift.setIntValue_(metrics_big)

	@objc.IBAction
	def applyMetrics_(self, sender):
		switch_on = bool(sender.objectValue())
		font = Glyphs.font

		if switch_on:
			Glyphs.intDefaults["GSSpacingIncrementLow"] = Glyphs.defaults['com.filipenegrao.Increment.metrics_small']
			Glyphs.intDefaults["GSSpacingIncrementHigh"] = Glyphs.defaults['com.filipenegrao.Increment.metrics_big']
		else:
			Glyphs.intDefaults["GSSpacingIncrementLow"] = 1
			Glyphs.intDefaults["GSSpacingIncrementHigh"] = 10

	@objc.IBAction
	def setKerningSmall_(self, sender):
		kerning_small = sender.intValue()
		Glyphs.defaults['com.filipenegrao.Increment.kerning_small'] = kerning_small
		self.kerning_txt_keys.setIntValue_(kerning_small)

	@objc.IBAction
	def setKerningBig_(self, sender):
		kerning_big = sender.intValue()
		Glyphs.defaults['com.filipenegrao.Increment.kerning_big'] = kerning_big
		self.kerning_txt_shift.setIntValue_(kerning_big)

	@objc.IBAction
	def applyKerning_(self, sender):
		switch_on = bool(sender.objectValue())
		font = Glyphs.font

		if switch_on:
			Glyphs.intDefaults["GSKerningIncrementLow"] = Glyphs.defaults['com.filipenegrao.Increment.kerning_small']
			Glyphs.intDefaults["GSKerningIncrementHigh"] = Glyphs.defaults['com.filipenegrao.Increment.kerning_big']
		else:
			Glyphs.intDefaults["GSKerningIncrementLow"] = 1
			Glyphs.intDefaults["GSKerningIncrementHigh"] = 10

	# @objc.IBAction
	# def setMetrics_(self, sender):
	# 	# print('Metrics')
	# 	Glyphs.defaults['com.filipenegrao.KeyboardIncrement.metrics'] = bool(sender.objectValue())

	# @objc.IBAction
	# def setKerning_(self, sender):
	# 	# print('Kerning')
	# 	Glyphs.defaults['com.filipenegrao.KeyboardIncrement.kerning'] = bool(sender.objectValue())

	# @objc.IBAction
	# def setKeyboard_(self, sender):
	# 	# print('Keyboard')
	# 	Glyphs.defaults['com.filipenegrao.KeyboardIncrement.keyboard'] = bool(sender.objectValue())

	# @objc.IBAction
	# def applyButton_(self, sender):

	# 	font = Glyphs.font

	# 	# get the default values
	# 	incValue = Glyphs.defaults['com.filipenegrao.KeyboardIncrement.increment']
	# 	applyMetrics = Glyphs.defaults['com.filipenegrao.KeyboardIncrement.metrics']
	# 	applyKerning = Glyphs.defaults['com.filipenegrao.KeyboardIncrement.kerning']
	# 	applyKeyboard = Glyphs.defaults['com.filipenegrao.KeyboardIncrement.keyboard']

	# 	if applyMetrics:
	# 		Glyphs.intDefaults["GSSpacingIncrementLow"] = incValue
	# 		Glyphs.intDefaults["GSSpacingIncrementLow"] = incValue * 10

	# 	if applyKerning:
	# 		Glyphs.intDefaults["GSKerningIncrementLow"] = incValue
	# 		Glyphs.intDefaults["GSKerningIncrementHigh"] = incValue * 10

	# 	if applyKeyboard:
	# 		font.keyboardIncrement = incValue
	# 		font.keyboardIncrementBig = incValue * 10

	# @objc.IBAction
	# def resetButton_(self, sender):
	# 	print('Reset Button')

	# @objc.python_method
	# def updateControls(self, sender = None, ui_field):
	# 	# self.displayValue.setStringValue_(str(Glyphs.defaults['com.filipenegrao.KeyboardIncrement.increment']))
	# 	self.stepper.setIntValue_(Glyphs.defaults['com.filipenegrao.KeyboardIncrement.increment'])
	# 	self.displayValue.setIntValue_(Glyphs.defaults['com.filipenegrao.KeyboardIncrement.increment'])

	@objc.python_method	
	def __del__(self):
		Glyphs.removeCallback(self.update)

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
