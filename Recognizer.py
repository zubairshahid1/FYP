
from gtts import gTTS
import speech_recognition as sr
from pygame import mixer
import time
import tempfile
from tempfile import TemporaryFile
from googletrans import Translator

class Recognizer():
	# global translator
	# translator = Translator()
	def talk(self,audio,lan):
		try:
			text_to_speech = gTTS(text=audio, lang=lan,slow=False)
			mixer.init()
			savefile = TemporaryFile()
			text_to_speech.write_to_fp(savefile)
			savefile.seek(0)
			mixer.music.load(savefile)
			mixer.music.play()
		except Exception:
			raise
	
	def myCommand(self,lan):
		#"listens for commands"
		
		recognize = sr.Recognizer()

		with sr.Microphone() as source:

			print('Gotii is listening...')
			recognize.pause_threshold = 1

			recognize.adjust_for_ambient_noise(source, duration=1)

			audio = recognize.listen(source)
			print('analyzing...')

		try:
			command = recognize.recognize_google(audio,language = lan).lower()
			print('You said: ' + command + '\n')


		except sr.UnknownValueError:
			print('Your last command couldn\'t be heard')
			return -1

		return command

	# def translate(self,command):
	# 	translated = translator.translate(command)
	# 	print(translated)
	# 	translated=translated.text
	# 	return translated