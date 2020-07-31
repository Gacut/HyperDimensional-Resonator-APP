from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
import time
import random

'''Variables that i work on while doing button instances
   Couldn't figure out the other way around so i thougt i'll make them global in this file '''
DialUpperLabel = Label(text='Set Date')
DialLowerLabel = Label(text='Set Time')
witnessDiode = Image(source='Graphics/reddot.png', size_hint=(0.1, 0.1))
GreenSwitchBool = False
RedSwitchBool = False
YellowSwitchBool = False
demonLoader = SoundLoader.load('Audio/Demon.ogg')
yearInput = TextInput(
	multiline=False, hint_text='Year', input_filter='int')


def WitnessFunction(button_instance):
	'''If Witness Well is pressed and GreenSwitchBool is set to True, it should open an popup with item selection'''
	if GreenSwitchBool:
		WitnessPopupWindow.open()
	else:
		pass


def buttonClose(button_instance):
	'''Button function that closes the DATE set popup and changes the DialUpperLabel text for default'''
	DialUpperLabel.text = 'Set Date'
	popupDate.dismiss()


def buttonClose2(button_instance):
	'''Button function that closes the TIME set popup and changes the DialLowerLabel text for default'''
	popupTime.dismiss()
	DialLowerLabel.text = 'Set Time'


def buttonClose3(button_instance):
	'''Button function to close the popup for item selection in WitnessPopupWindow and changing its picture to default'''
	WitnessPopupWindow.dismiss()
	witnessButton.background_normal = 'Graphics/Well.png'
	witnessButton.background_down = 'Graphics/WellPressed.png'


def DateSet(button_instance):
	'''Button function for opening a popup window for setting a date while RedSwitchBool is set to True'''
	if RedSwitchBool:
		popupDate.open()
	else:
		pass


def TimeSet(button_instance):
	'''Button function for opening a popup window for setting a time while RedSwitchBool is set to True'''
	if RedSwitchBool:
		popupTime.open()
	else:
		pass


def DateAddButton(button_instance):
	'''Few restrictions about "ADD" button in DialUpper.
	   while the condition is not fullfiled, it changes the popupDate title to inform the user what needs to be changed. 
	   Additionally, if inputed numbers aren't long enough, it ads a "0" before the input. This can be find under the else statement.
	   after that, it sets the input boxes to empty and closes the popupDate'''

	global DialUpperLabel

	if yearInput.text == '' or monthInput.text == '' or dayInput.text == '':
		popupDate.title = 'You need to add a correct date\n Year, month and day must have some values'

	elif int(monthInput.text) == 0 or int(dayInput.text) == 0:
		popupDate.title = 'You need to add a correct date\n Month and day must be greater than zero'

	else:
		if len(monthInput.text) < 2:
			monthInput.text = '0' + monthInput.text
		if len(dayInput.text) < 2:
			dayInput.text = '0' + dayInput.text
		DialUpperLabel.text = 'Date:\n' + \
			str(dayInput.text) + '-' + str(monthInput.text) + \
			'-' + str(yearInput.text)

		yearInput.text = ''
		monthInput.text = ''
		dayInput.text = ''
		popupDate.dismiss()


def TimeAddButton(button_instance):
	'''Few restrictions about "ADD" button in DialLower.
	   while the condition is not fullfiled, it changes the popupTime title to inform the user what needs to be changed. 
	   Additionally, if inputed numbers aren't long enough, it ads a "0" before the input. This can be find under the else statement.
	   after that, it sets the input boxes to empty and closes the popupTime'''
	global DialLowerLabel
	if '-' in hourInput.text or '-' in minutesInput.text:
		popupTime.title = 'Hour and minutes must be equal or greater than zero'
	elif hourInput.text == '' or minutesInput.text == '':
		popupTime.title = 'Hours and minutes must contain some numbers'
	else:
		if len(hourInput.text) < 2:
			hourInput.text = '0' + hourInput.text
		if len(minutesInput.text) < 2:
			minutesInput.text = '0' + minutesInput.text
		DialLowerLabel.text = 'Time:\n' + \
			str(hourInput.text) + ':' + str(minutesInput.text)
		hourInput.text = ''
		minutesInput.text = ''
		popupTime.dismiss()


def year_lenght(yearInput, text):
	'''Conditions for year input. Year can't have more than 4 digits
	   if it has, it automaticly removes fifth digit and leaves user with 4 '''
	if len(text) > 4:
		yearInput.do_backspace()


def month_lenght(monthInput, text):
	'''Conditions for month length input
	   it can not be more than 2 characters and greater than 12'''
	try:
		if len(text) > 2:
			monthInput.do_backspace()
		if int(text) > 12:
			monthInput.do_backspace()
	except ValueError:
		pass


def day_lenght(dayInput, text):
	'''Conditions for day length input
	   it can not be more than 2 characters and greater than 31'''
	try:
		if len(text) > 2:
			dayInput.do_backspace(from_undo=True)
		elif int(text) > 31:
			dayInput.do_backspace()
	except ValueError:
		pass


def hour_lenght(hourInput, text):
	'''Conditions for hour length input
	   it can not be more than 2 characters and greater than 23'''
	try:
		if len(text) > 2:
			hourInput.do_backspace(from_undo=True)
		elif int(text) > 23:
			hourInput.do_backspace()
	except ValueError:
		pass


def minutes_lenght(minutesInput, text):
	'''Conditions for minutes length input
	   it can not be more than 2 characters and greater than 59'''
	try:
		if len(text) > 2:
			minutesInput.do_backspace(from_undo=True)
		elif int(text) > 59:
			minutesInput.do_backspace()
	except ValueError:
		pass


def switchGreenMechanics(button_instance):
	'''Button function for a Green switch.
	   changes the witness diode to green when pressed and sets GreenSwitchBool to true
	   if GreenSwitchBool is set to true while switch is pressed, it reverts back to default'''
	global GreenSwitchBool
	if GreenSwitchBool == False:
		GreenSwitchBool = True
		switchGREEN.background_normal = 'Graphics/GreenON.png'
		witnessDiode.source = 'Graphics/greendot.png'
		print('Green Switch Set to True')
	else:
		GreenSwitchBool = False
		witnessDiode.source = 'Graphics/reddot.png'
		switchGREEN.background_normal = 'Graphics/GreenOff.png'
		print('Green Switch Set to False')


def switchRedMechanics(button_instance):
	'''Button function for a Red switch.
	   sets RedSwitchBool to true
	   if RedSwitchBool is set to true while switch is pressed, it reverts back to default and turns off the Demon sound when
	   you choose Blood in witness Well'''
	global RedSwitchBool, demonLoader
	if RedSwitchBool == False:
		RedSwitchBool = True
		switchRED.background_normal = 'Graphics/RedON.png'
		print('Red Switch Set to True')
	else:
		RedSwitchBool = False
		switchRED.background_normal = 'Graphics/RedOff.png'
		demonLoader.stop()
		print('Red Switch Set to False')


def switchYellowMechanics(button_instance):
	'''Button function for a Yellow switch.
	   ets YellowSwitchBool to true
	   if YellowSwitchBool is set to true while switch is pressed, it reverts back to default'''
	global YellowSwitchBool
	if YellowSwitchBool == False:
		YellowSwitchBool = True
		switchYELLOW.background_normal = 'Graphics/YellowON.png'
		print('Yellow Switch Set to True')
	else:
		YellowSwitchBool = False
		switchYELLOW.background_normal = 'Graphics/YellowOff.png'
		print('Yellow Switch Set to False')


def CrystalAdd(button_instance):
	'''When you choose a crystal in Well popup, it places the crystal in well and closes the popup after'''
	witnessButton.background_normal = 'Graphics/CrystalInWell.png'
	witnessButton.background_down = 'Graphics/CrystalInWellPressed.png'
	WitnessPopupWindow.dismiss()


def BloodAdd(button_instance):
	'''When you choose a blood in Well popup, it places the blood in well and closes the popup after'''
	witnessButton.background_normal = 'Graphics/BloodInWell.png'
	witnessButton.background_down = 'Graphics/BloodInWellPressed.png'
	WitnessPopupWindow.dismiss()


def RubbingPlateAudio(button_instance):
	'''It plays random mhz sound when conditions are met and freezes the app for 1 second
	   i couldn't figure out another way to keep user from spamming the rubbing plate for now.
	   if user chooses blood in the well and conditions are met, it plays Demonic sound'''
	global demonLoader
	if RedSwitchBool and YellowSwitchBool:
		if 'Date:' in DialUpperLabel.text and witnessButton.background_normal == 'Graphics/CrystalInWell.png':
			audioFiles = ['Audio/100mhz.ogg', 'Audio/200mhz.ogg',
						  'Audio/450mhz.ogg', 'Audio/600mhz.ogg']
			choosenFile = random.choice(audioFiles)
			loadedFile = SoundLoader.load(choosenFile)
			loadedFile.play()
			time.sleep(1)
		if 'Date:' in DialUpperLabel.text and witnessButton.background_normal == 'Graphics/BloodInWell.png':
			demonLoader.play()


'''Variables for DATE Popup STARTS here'''
DateBody = GridLayout(rows=2)
dateInputBody = BoxLayout(orientation='horizontal')
monthInput = TextInput(
	multiline=False, hint_text='Month', input_filter='int')
dayInput = TextInput(
	multiline=False, hint_text='Day', input_filter='int')
addButton = Button(text='Add', on_release=DateAddButton)
exitButton = Button(text='Close', on_release=buttonClose)
popupDate = Popup(title='Set Date', auto_dismiss=False,
				  title_align='center', content=DateBody, size_hint=(0.8, 0.5))

yearInput.bind(text=year_lenght)
monthInput.bind(text=month_lenght)
dayInput.bind(text=day_lenght)
dateInputBody.add_widget(dayInput)
dateInputBody.add_widget(monthInput)
dateInputBody.add_widget(yearInput)
dateInputBody.add_widget(addButton)
DateBody.add_widget(dateInputBody)
DateBody.add_widget(exitButton)
'''Variables for DATE Popup ENDS here'''

'''Variables for TIME Popup STARTS here'''
TimeBody = GridLayout(rows=2)
TimeInputBody = BoxLayout(orientation='horizontal')
hourInput = TextInput(
	multiline=False, hint_text='Hour', input_filter='int')
minutesInput = TextInput(
	multiline=False, hint_text='Minutes', input_filter='int')
addButton2 = Button(text='Add', on_release=TimeAddButton)
exitButton2 = Button(text='Close', on_release=buttonClose2)
popupTime = Popup(title='Set Time', auto_dismiss=False,
				  title_align='center', content=TimeBody, size_hint=(0.8, 0.5))

hourInput.bind(text=hour_lenght)
minutesInput.bind(text=minutes_lenght)
TimeInputBody.add_widget(hourInput)
TimeInputBody.add_widget(minutesInput)
TimeInputBody.add_widget(addButton2)
TimeBody.add_widget(TimeInputBody)
TimeBody.add_widget(exitButton2)
'''Variables for adding TIME Popup ENDS here'''

'''Variables for Choosing Witness Item Popup STARTS here'''
WitnessBody = BoxLayout(orientation='vertical')
WitnessPopupGrid = GridLayout(cols=2, rows=3)
WButton1 = Button(on_release=CrystalAdd, background_normal='Graphics/Quartz.png',
				  background_down='Graphics/QuartzPressed.png', border=(0, 0, 0, 0))
WButton2 = Button(on_release=BloodAdd, background_normal='Graphics/Blood.png',
				  background_down='Graphics/BloodPressed.png', border=(0, 0, 0, 0))
exitButton3 = Button(text='Close', on_release=buttonClose3)
WitnessPopupWindow = Popup(title='Choose an item', auto_dismiss=False,
						   title_align='center', content=WitnessBody, size_hint=(0.8, 0.5))

WitnessPopupGrid.add_widget(WButton1)
WitnessPopupGrid.add_widget(WButton2)
WitnessBody.add_widget(WitnessPopupGrid)
WitnessBody.add_widget(exitButton3)

witnessButton = Button(on_release=WitnessFunction,
					   background_normal='Graphics/Well2.png', background_down='Graphics/WellPressed2.png', border=(16, 16, 16, 16))
'''Variables for Choosing Witness Item Popup ENDS here'''


'''These are three buttons that are displayed as switches in the app'''
switchGREEN = Button(on_release=switchGreenMechanics,
					 background_normal='Graphics/GreenOff.png', background_down='Graphics/GreenOff.png')
switchRED = Button(on_release=switchRedMechanics,
				   background_normal='Graphics/RedOff.png', background_down='Graphics/RedOff.png')
switchYELLOW = Button(on_release=switchYellowMechanics,
					  background_normal='Graphics/YellowOff.png', background_down='Graphics/YellowOff.png')
