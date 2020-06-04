

import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import os

class English_Operations():

	def OpenChrome(self,command):

		reg_ex = re.search('search (.*)', command)
		search_for = command.split("search")[1] 
		print(search_for)
		url = 'https://www.google.com/'
		if reg_ex:
			subgoogle = reg_ex.group(1)
			url = url + 'r/' + subgoogle
		driver = webdriver.Chrome('D:/fyp/FYP/chromedriver_win32/chromedriver.exe')
		driver.get('http://www.google.com')
		search = driver.find_element_by_name('q')
		search.send_keys(str(search_for))
		search.send_keys(Keys.RETURN) 
	
	def LaunchApp(self,command):
		search_for = command.split("launch")[1]
		
		if search_for == ' notepad' :
			os.system('start'+ search_for)
		elif search_for == ' calculator':
			os.system('start calc')
		elif search_for == ' utorrent':
			os.system('start C:/Users/shoaibshahid/AppData/Roaming/uTorrent/uTorrent.exe')
		elif search_for  == ' idm' or search_for ==' internet download manager':
			os.system('start C:/"Program Files (x86)"/"Internet Download Manager"/IDMan.exe')
		elif search_for ==' word' or search_for ==' microsoft word':
			os.system('start winword')
		elif search_for ==' power point' or search_for ==' powerpoint' or search_for ==' microsoft powerpoint' or search_for ==' microsoft power point':
			os.system('start powerpnt')
		elif search_for ==' excel' or search_for ==' microsoft excel':
			os.system('start excel')
		elif search_for == ' netbeans':
			os.system('start C:/"Program Files"/"NetBeans 8.1"/bin/netbeans64.exe')
		elif search_for == ' internet explorer' or search_for == ' internetexplorer':
			os.system('start C:/"Program Files"/"Internet Explorer"/iexplore.exe')
		elif search_for == ' sublime text' or search_for == ' sublimetext':
			os.system('start C:/"Program Files"/"Sublime Text 3"/sublime_text.exe')

		# elif 'hello' in command:
		#     self.talk('Hi')

		# elif 'who are you' in command:
		#     self.talk('I am Gotti, Your voice assistant')