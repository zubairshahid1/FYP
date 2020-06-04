

import webbrowser
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import os

class Urdu_Operations():

	def OpenChrome(self,command):

		reg_ex = re.search('تلاش (.*)', command)
		search_for = command.split("تلاش")[0] 
		print(search_for)
		url = 'https://www.google.com/'
		if reg_ex:
			subgoogle = reg_ex.group(1)
			url = url + 'r/' + subgoogle
		driver = webdriver.Chrome('C:/Users/shoaibshahid/Downloads/FYP/chromedriver_win32/chromedriver.exe')
		driver.get('http://www.google.com')
		search = driver.find_element_by_name('q')
		search.send_keys(str(search_for))
		search.send_keys(Keys.RETURN)

	def LaunchApp(self,command):
		search_for = command.split("کھولو")[0]
		print(search_for)
		if search_for =='نوٹ پیڈ ':
			os.system('start notepad')
		elif search_for == 'کیلکولیٹر ' or search_for == 'لکولیٹر ' :
			os.system('start calc')
		elif search_for == 'یو ٹورینٹ '   or search_for == 'یوٹورینٹ ' :
			os.system('start C:/Users/shoaibshahid/AppData/Roaming/uTorrent/uTorrent.exe')
		elif search_for =='انٹرنیٹ ڈاؤن لوڈ مینیجر ' or search_for =='انٹرنیٹ ڈونلوڈ مینیجر ':
			os.system('start C:/"Program Files (x86)"/"Internet Download Manager"/IDMan.exe')
		elif search_for ==' word' or search_for ==' microsoft word':
			os.system('start winword')
		elif search_for =='پاور پوائنٹ '  or search_for =='مائیکروسافٹ پاورپوائنٹ ' :
			os.system('start powerpnt')
		elif search_for =='ایکسل ' or search_for =='مائیکروسافٹ ایکسل ':
			os.system('start excel')
		elif search_for == 'نیٹ بین ':
			os.system('start C:/"Program Files"/"NetBeans 8.1"/bin/netbeans64.exe')
		elif search_for == 'انٹرنیٹ ایکسپلورر ' :
			os.system('start C:/"Program Files"/"Internet Explorer"/iexplore.exe')
		elif search_for == ' sublime text' or search_for == ' sublimetext':
			os.system('start C:/"Program Files"/"Sublime Text 3"/sublime_text.exe')
