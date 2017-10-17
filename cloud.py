#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

#import numpy as np 
#import PIL.Image as Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def Statistics(lst):
	dic = {}
	for k in lst:
		if not k.decode('utf-8') in dic:
			dic[k.decode('utf-8')] = 0
		dic[k.decode('utf-8')] += 1
	return dic

ls = []
with open('163.txt', 'r') as f:
	for line in f:
		ls.append(line.strip())
dic = Statistics(ls)
font = r'simhei.ttf'
wc = WordCloud(collocations=False, font_path=font, width=1400, height=1400, margin=2,).generate_from_frequencies(dic)
plt.imshow(wc)
plt.axis('off')
plt.show()
wc.to_file('singer.png')