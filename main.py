from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from hdrbuttons import *


class HDR(App):
	'''This class is a builder for the whole app'''

	def build(self):
		'''Here are all variables i need to make frontend of an app'''
		layout = FloatLayout()
		background = Image(source='Graphics/HDRcase.png',
						   allow_stretch=True, keep_ratio=False)
		witnessBody = GridLayout(rows=5, rows_minimum={
			1: 100, 2: 30, 3: 30, 4: 100, 5: 0})
		dialBody = GridLayout(rows=4)
		switchesBody = GridLayout(rows=5)
		WholeBody = GridLayout(rows=2)
		bodyUpper = BoxLayout(orientation='horizontal')
		RPBody = GridLayout(rows=2)
		RubbingPlateLabel = Label(
			text='Rubbing Plate', size_hint_y=None, height=40, color=[1, 0, 0, 1], font_name='Fonts/Impact Label.ttf')
		RubbingPlate = Button(background_normal='Graphics/RubbingPlate.png',
							  background_down='Graphics/RubbingPlate.png', border=(50, 0, 0, 0), on_press=RubbingPlateAudio)
		witnessLabel = Label(text='Witness', color=[1, 0, 0, 1],
							 size_hint_y=None, font_name='Fonts/Impact Label.ttf')
		DialUpper = Button(on_release=DateSet, background_normal='Graphics/DateNormal.png',
						   background_down='Graphics/DatePressed.png', border=(0, 0, 0, 0))
		DialLower = Button(on_release=TimeSet, background_normal='Graphics/TimeNormal.png',
						   background_down='Graphics/TimePressed.png', border=(0, 0, 0, 0))
		'''Below is the placement order of all buttons, background and switches visible in the app
		   I allways call this as a "Sandwitch" because i just add layer after layer of the interactive stuff of an app'''
		RPBody.add_widget(RubbingPlateLabel)
		RPBody.add_widget(RubbingPlate)
		witnessBody.add_widget(Label())
		witnessBody.add_widget(witnessButton)
		witnessBody.add_widget(witnessLabel)
		witnessBody.add_widget(witnessDiode)
		witnessBody.add_widget(Label())
		switchesBody.add_widget(switchGREEN)
		switchesBody.add_widget(switchRED)
		switchesBody.add_widget(switchYELLOW)
		switchesBody.add_widget(Label())

		dialBody.add_widget(DialUpper)
		dialBody.add_widget(DialUpperLabel)
		dialBody.add_widget(DialLower)
		dialBody.add_widget(DialLowerLabel)

		bodyUpper.add_widget(witnessBody)
		bodyUpper.add_widget(switchesBody)
		bodyUpper.add_widget(dialBody)

		WholeBody.add_widget(bodyUpper)
		WholeBody.add_widget(RPBody)

		layout.add_widget(background)
		layout.add_widget(WholeBody)
		return layout


HDR().run()
