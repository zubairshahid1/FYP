

import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

class Operations():

	def OpenChrome(self,command):

		reg_ex = re.search('search (.*)', command)
		search_for = command.split("search",1)[1] 
		print(search_for)
		url = 'https://www.google.com/'
		if reg_ex:
			subgoogle = reg_ex.group(1)
			url = url + 'r/' + subgoogle
		# talk('Okay!')
		driver = webdriver.Chrome('C:/Users/shoaibshahid/Downloads/FYP/chromedriver_win32/chromedriver.exe')
		driver.get('http://www.google.com')
		search = driver.find_element_by_name('q')
		search.send_keys(str(search_for))
		#talk('Okay!')
		search.send_keys(Keys.RETURN) # hit return after you enter search text

		# elif 'hello' in command:
		#     self.talk('Hi')

		# elif 'who are you' in command:
		#     self.talk('I am Gotti, Your voice assistant')