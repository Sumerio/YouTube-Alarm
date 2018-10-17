from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import subprocess
import time

def alarm(url):
	
	res  = requests.get(url)
    	data = res.text
	soup = BeautifulSoup(data,'lxml')
	link=soup.find('a', attrs={'href': re.compile("^/watch?")})
	url1="https://www.youtube.com/"
	url2=url1+link.get('href')
	driver = webdriver.Chrome()
	driver.get(url2)
	time.sleep(60)
	driver.quit()

def gettime(a):
	x=time.localtime(time.time())
	if (a==0):
		return x.tm_hour
	if (a==1):
		return x.tm_min

def fileread():
	url= "https://www.youtube.com/results?search_query="
	time.sleep(2)
	rfile=open("time.txt","r")
	h_app=rfile.read(2)
	m_app=rfile.read(2)
	rfile.close()

	rurl=open("url.txt","r")
	url1=rurl.read()
	rurl.close()
	url1.replace(" ","+")
	url=url+url1
	H=int(h_app)
	M=int(m_app)
	if(H==gettime(0) and M==gettime(1)):	
		alarm(url)


while True:
	fileread()
