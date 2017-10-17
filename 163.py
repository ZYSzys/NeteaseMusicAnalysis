#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import os
import random
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
import traceback

def WriteData(data):
	f = open(os.getcwd()+'/163.txt', "a+")
	f.write(data+'\n')
	f.close()

def CatchPlaylist(url):
	driver = webdriver.PhantomJS()
	driver.get(url)
	driver.switch_to_frame('g_iframe')
	try:
		wait = ui.WebDriverWait(driver, 10)
		wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="m-cvrlst f-cb"]'))
		urls = driver.find_elements_by_xpath('//*[@class="m-cvrlst f-cb"]/li/div/a')
		favorite_url = urls[0].get_attribute("href")
	except Exception:
		print traceback.print_exc()
	finally:
		driver.quit()
	return favorite_url

def CatchSongs(url_id, url):
	user = url_id.split('=')[-1].strip()
	print user+': '

	driver = webdriver.PhantomJS()
	driver.get(url)
	driver.switch_to_frame('g_iframe')
	try:
		wait = ui.WebDriverWait(driver, 10)
		wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="j-flag"]'))
		max_song = driver.find_elements_by_class_name('num')
		max_song = int(max_song[-1].text)
		song_key = 1
		try:
			while song_key <= max_song:
				songs = driver.find_elements_by_xpath('//*[@class="j-flag"]/table/tbody/tr[%s]/td[4]/div/span'%song_key)
				singer = songs[0].get_attribute('title')
				print song_key, singer.encode('utf-8')
				WriteData(singer.encode('utf-8'))
				song_key += 1
			driver.quit()
		except Exception:
			print 'No more music'
			pass
	except Exception:
		traceback.print_exc()
		

if __name__ == '__main__':
	for url in ['http://music.163.com/#/user/home?id=339449788']:
		time.sleep(random.randint(2, 4))
		url_playlist = CatchPlaylist(url)
		
		time.sleep(random.randint(1, 2))
		CatchSongs(url, url_playlist)


