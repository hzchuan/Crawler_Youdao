#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:22:23 2018

@author: hzchuan
"""
import urllib
from bs4 import BeautifulSoup
def getHtml(word):
    searchUrl = "http://dict.youdao.com/search?q=" + word + "&keyfrom=dict.index"
    with urllib.request.urlopen(searchUrl) as url:
        response = url.read().decode('utf-8')
    return response
#讀取詞彙庫
df = [line.rstrip('\n') for line in open('voc.txt')]
y =[]
def showResult(df):
    for word in df:
        wordSoup = BeautifulSoup(getHtml(word),"html.parser")
        voc = wordSoup.find('span', {'class', 'keyword'}).string #查詢單字
        exp = wordSoup.find('span', {'class', 'title'}) #單字解釋
        exam = wordSoup.find_all('div', {'class', 'examples'}) #單字例句
        mean =  wordSoup.find_all('span', {'class', 'def'}) #單字意義
        print(voc)  
        #當爬取出的資料為空值就回傳 None 非空值就進行格式處理
        try: exp = str(exp)
        except AttributeError: exp = 'None'
        else:
            if len(exp)!=0:     
                exp = exp.replace('<span class="title">','')
                exp = exp.replace('</span>','')
            else: exp = 'None'
          
        try: exam = str(exam)
        except AttributeError: exam = 'None'
        else:
            if len(exam)!=0:     
                exam = exam.replace('\n','')
                exam = exam.replace('[<div class="examples">','')
                exam = exam.replace('<div class="examples">','')
                exam = exam.replace('<p>','')
                exam = exam.replace('</p>','')
                exam = exam.replace('</div>','')
                exam = exam.replace(']','')
            else: exam = 'None'
                   
        try: mean = str(mean)
        except AttributeError: mean = 'None'
        else:
            if len(mean)!=0:
                mean = mean.replace('[<span class="def">','')
                mean = mean.replace('<span class="def">','')
                mean = mean.replace(']','')
                mean = mean.replace('</span>','')
            else: mean = 'None'
        #將每次結果添加到 y中
        y.append([str(voc),str(exp),exam,str(mean)]) 
        print(len(y))
        
if __name__ == '__main__':
	showResult(df)
#寫出資料
with open('result.txt', 'w') as f:
    for item in y:
        f.write("%s\n" % item)

    