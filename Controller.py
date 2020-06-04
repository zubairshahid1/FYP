
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from UiClass import Ui_MainWindow
from Recognizer import Recognizer
from English_Operations import English_Operations
from Urdu_Operations import Urdu_Operations
class Controller():
	global language
	language="eng"
	global recognizer
	recognizer=Recognizer()
	global engoperations
	engoperations=English_Operations()
	global uroperations
	uroperations=Urdu_Operations()
	def __init__(self):
		app = QtWidgets.QApplication(sys.argv)
		MainWindow = QtWidgets.QMainWindow()
		global ui
		ui = Ui_MainWindow()
		ui.setupUi(MainWindow)
		ui.microbutton.clicked.connect(lambda: self.callistner("button"))
		ui.querytextfield.returnPressed.connect(lambda: self.callistner("textfield"))
		ui.actionEnglish.triggered.connect(lambda:self.change_language("eng"))
		ui.actionUrdu.triggered.connect(lambda:self.change_language("ur"))
		ui.add_label("goti","Hello! I am Gotti. How can I help you?")
		recognizer.talk("Hello! I am Gotti. How can I help you?","en-uk")
		MainWindow.show()
		sys.exit(app.exec_())
	def change_language(self,lang):
		global language
		language=lang


	def makedecision(self,command):
		if language=='eng':
			if 'search' in command:
				engoperations.OpenChrome(command)
			elif 'launch' in command:
				engoperations.LaunchApp(command)
			else:
				ui.add_label("goti","Sorry can't understand your command")
				recognizer.talk("Sorry can't understand Your command","en-uk")
		else:
			if 'تلاش' in command:
				uroperations.OpenChrome(command)
			elif 'کھولو' in command:
				uroperations.LaunchApp(command)
			else:
				ui.add_label("goti","معاف کیجئے گا آپ کا حکم سمجھ نہیں آیا")

	def callistner(self,who):

		if((who=="button")& (language=="eng")):
			ui.changetext("Gouti is Listening..")
			text=recognizer.myCommand('en-US')
			if text==-1:
				text="your last command couldn\'t be heard.please speak again"
				ui.add_label("goti",text)
				recognizer.talk(text,"en-uk")
			else:
				ui.add_label("user",text)
				ui.changetext("")
				self.makedecision(text)
		
		elif((who=="textfield")& (language=="eng")):   
			text=ui.querytextfield.text()
			ui.add_label("user",text)
			ui.changetext("") 
			self.makedecision(text)
		
		elif((who=="button")& (language=="ur")):
			ui.changetext("گوٹی سن رہا ہے ...")
			text=recognizer.myCommand('ur-PK')
			if text==-1:
				text="آپ کا آخری حکم نہیں سنا گیا۔ براہ کرم دوبارہ بولیں"
				ui.add_label("goti",text)
			else:
				ui.add_label("user",text)
				ui.changetext("")
				self.makedecision(text)
		elif((who=="textfield")& (language=="ur")):   
			text=ui.querytextfield.text()
			ui.add_label("user",text)
			ui.changetext("") 
			self.makedecision(text)

		ui.scrolled(ui.scrollArea.verticalScrollBar().maximum())


		


if __name__ == "__main__":
	Controller()
	
	