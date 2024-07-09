# importation des bibliotheques 

def recherche(livre):
	from bs4 import BeautifulSoup
	import requests
	from urllib.request import Request, urlopen
	import csv
	import re
	from tkinter import *
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.common.by import By
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from fake_useragent import UserAgent
	from selenium.webdriver.chrome.options import Options
	from selenium.webdriver.support.expected_conditions import presence_of_element_located
	import time

	################################################## RECCOLTE D'INFORMATION ##################################################
	# livre par défaut 

	#livre = "Le Rouge et le Noir"
	livred = livre.split()
	print(livred)

	"""### Recherche dans la Fnac
	# ex de lien :  https://www.fnac.com/SearchResult/ResultList.aspx?Search=Le+rouge+et+le+noir&sft=1&sl

	Flien1 = "https://www.fnac.com/SearchResult/ResultList.aspx?Search="
	Flien2 = "&sft=1&sl"

	Flienvar = ""   #définition de la partit du lien qui change
	for i in range(len(livred)-1):
	    Flienvar = Flienvar+livred[i]+"+"
	Flienvar = Flienvar+livred[len(livred)-1]

	Flien = Flien1+Flienvar+Flien2 # concaténation du lien
	print(Flien)

	options = Options()
	ua = UserAgent()
	userAgent = ua.random
	print(userAgent)
	options.add_argument(f'user-agent={userAgent}')


	PATH ="C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH, options = options)

	driver.get(Flien)
	time.sleep(0.25)
	print(driver.title)
	time.sleep(0.25)
	Fpage = driver.page_source

	time.sleep(10)
	print("ok")


	acccookies = driver.find_element_by_id("onetrust-accept-btn-handler")
	acccookies.click()

	choisir = driver.find_element_by_class_name("FA")
	choisir.click()

	retmag = driver.find_element_by_class_name("f-nearby-stores")
	print(retmag)
	retmag.click()


	""""""recvil = driver.find_element_by_class_name("StoreSearch")
	recvil.send_keys("Paris")
	recvil.send_keys(Keys.RETURN)""""""


	time.sleep(10)

	driver.quit()"""

	#Recherche sur Paris Librairies 
	Llien1 = "https://www.parislibrairies.fr/listeliv.php?base=allbooks&mots_recherche="
	Llienvar = ""   #définition de la partit du lien qui change
	for i in range(len(livred)-1):
	    Llienvar = Llienvar+livred[i]+"+"
	Llienvar = Llienvar+livred[len(livred)-1]

	Llien = Llien1+Llienvar # concaténation du lien
	print(Llien)

	########################################################

	options = Options()
	ua = UserAgent()
	userAgent = ua.random
	print(userAgent)
	options.add_argument(f'user-agent={userAgent}')
	PATH ="C:\Program Files (x86)\chromedriver.exe"


	driver = webdriver.Chrome(PATH, options = options)

	driver.get(Llien)
	time.sleep(0.25)

	varprix = driver.find_element((By.XPATH, """//*[@id="liste_livres"]/li[1]/div[2]/div[2]/div/div/div[1]/span[2]/a"""))
	prix = varprix.get_attribute("textContent")
	print(prix)

	########################################################

	wait = WebDriverWait(driver, 10)
	first_result = wait.until(presence_of_element_located((By.ID, "tarteaucitronPersonalize2")))
	print(first_result.get_attribute("textContent"))
	time.sleep(0.25)
	first_result.click()
	time.sleep(0.25)

	########################################################

	driver.find_element(By.ID, "linkMagasins").click()
	time.sleep(0.25)
	textbrut = wait.until(presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/h2/a")))
	nomlibrairie = textbrut.get_attribute("textContent")
	print(nomlibrairie)
	addressehtml = wait.until(presence_of_element_located((By.XPATH, """//*[@id="SHOPLIST"]/div[2]/div/div[2]/div[1]/div[1]/div""")))
	adresse1 = addressehtml.get_attribute("textContent")
	print(adresse1)


	########################################################

	varstock = wait.until(presence_of_element_located((By.XPATH, """//*[@id="SHOPLIST"]/div[2]/div/div[2]/div[1]/div[3]/div/p""")))
	stockoupas = varstock.get_attribute("textContent")
	print(stockoupas)

	########################################################

	tableau = [[""]*10]
	return tableau

	########################################################

	time.sleep(3)
	driver.quit()

