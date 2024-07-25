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

		Glyphs.registerDefault('com_filipenegrao_Increment_keyboard_small', 1)
		Glyphs.registerDefault('com_filipenegrao_Increment_keyboard_big', 10)
		Glyphs.registerDefault('com_filipenegrao_Increment_keyboard_huge', 100)
		
		Glyphs.registerDefault('com_filipenegrao_Increment_metrics_small', 1)
		Glyphs.registerDefault('com_filipenegrao_Increment_metrics_big', 10)

		Glyphs.registerDefault('com_filipenegrao_Increment_kerning_small', 1)
		Glyphs.registerDefault('com_filipenegrao_Increment_kerning_big', 10)
		print("__keyboard", Glyphs.intDefaults['com_filipenegrao_Increment_keyboard_small'], Glyphs.intDefaults['com_filipenegrao_Increment_keyboard_big'])

	@objc.IBAction
	def applyKeyboard_(self, sender):
		font = Glyphs.font
		if Glyphs.boolDefaults["com_filipenegrao_Increment_keyboard"]:
			try:
				# Glyphs 3
				font.keyboardIncrement = Glyphs.intDefaults['com_filipenegrao_Increment_keyboard_small']
				font.keyboardIncrementBig = Glyphs.intDefaults['com_filipenegrao_Increment_keyboard_big']
				font.keyboardIncrementHuge = Glyphs.intDefaults['com_filipenegrao_Increment_keyboard_huge']
			except:
				# Glyphs 2
				pass
		else:
			try:
				# Glyphs 3
				font.keyboardIncrement = 1
				font.keyboardIncrementBig = 10
				font.keyboardIncrementHuge = 100
			except:
				# Glyphs 2
				pass

	@objc.IBAction
	def applyMetrics_(self, sender):
		font = Glyphs.font
		if Glyphs.boolDefaults["com_filipenegrao_Increment_metrics"]:
			Glyphs.intDefaults["GSSpacingIncrementLow"] = Glyphs.intDefaults['com_filipenegrao_Increment_metrics_small']
			Glyphs.intDefaults["GSSpacingIncrementHigh"] = Glyphs.intDefaults['com_filipenegrao_Increment_metrics_big']
		else:
			Glyphs.intDefaults["GSSpacingIncrementLow"] = 1
			Glyphs.intDefaults["GSSpacingIncrementHigh"] = 10

	@objc.IBAction
	def applyKerning_(self, sender):
		font = Glyphs.font
		if Glyphs.boolDefaults["com_filipenegrao_Increment_kerning"]:
			Glyphs.intDefaults["GSKerningIncrementLow"] = Glyphs.intDefaults['com_filipenegrao_Increment_kerning_small']
			Glyphs.intDefaults["GSKerningIncrementHigh"] = Glyphs.intDefaults['com_filipenegrao_Increment_kerning_big']
		else:
			Glyphs.intDefaults["GSKerningIncrementLow"] = 1
			Glyphs.intDefaults["GSKerningIncrementHigh"] = 10

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
