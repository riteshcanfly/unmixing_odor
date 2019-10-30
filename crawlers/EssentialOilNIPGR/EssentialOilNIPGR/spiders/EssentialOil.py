# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy import Request,FormRequest
from scrapy.spiders import CrawlSpider
from scrapy import Item,Field
#from SKapoor.items import Cookbook
from bs4 import BeautifulSoup
import logging, pprint, json, urllib


class EssentialoilSpider(CrawlSpider):
    name = 'EssentialOil'
    allowed_domains = ['http://www.nipgr.ac.in/Essoildb/', 'http://223.31.159.15']
    #start_urls = ['http://http://www.nipgr.ac.in/Essoildb//']

    def start_requests(self):
        plant_name= ['Abies alba', 'Abies borisii-regis']
        
        #urli = 'http://http://www.nipgr.ac.in/Essoildb//'
        headers= { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                   'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9,pa;q=0.8,hi;q=0.7',
                    'Cache-Control': 'max-age=0',
                    'Connection': 'keep-alive',
                    #'Content-Length': '572',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    #'Host': '223.31.159.15',
                    'Origin': 'http://223.31.159.15',
                    'Referer': 'http://223.31.159.15/Essoildb/essoildb_2.html',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
                }
        headers = { #'Host': '223.31.159.15',
                    'Origin': 'http://223.31.159.15',    
                    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' ,
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Accept-Encoding': 'gzip, deflate',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    #'Content-Length': '567',
                    'Connection': 'keep-alive',
                    'Referer': 'http://223.31.159.15/Essoildb/essoildb_2.html',
                    'Upgrade-Insecure-Requests': '1'
        }        
        link = 'http://223.31.159.15/cgi-bin/disc/essoildb/search_2.cgi'
        for i in plant_name:
            payload = {"txtPlantName": "Abies+alba", 
                        "selPlantName": "AND",
                        "txtLocation":"", 
                        "selLocation": "AND",
                        "txtYear":"", 
                        "selYear": "AND",
                        "txtVolume":"", 
                        "selVolume": "AND",
                        "txtArticle":"", 
                        "selArticle": "AND",
                        "txtAuthor": "",
                        "selAuthor": "AND",
                        "txtJournal": "",
                        "selJournal": "AND",
                        "txtFamily": "",
                        "selFamily": "AND",
                        "txtPlantStage": "",
                        "selPlantStage": "AND",
                        "txtExpCond": "",
                        "selExpCond": "AND",
                        "txtCompoundName": "",
                        "selCompoundName": "AND",
                        "txtCas": "",
                        "selCas": "AND",
                        "txtPercentage": "",
                        "selPercentage": "AND",
                        "txtPlantPart": "",
                        "selPlantPart": "AND",
                        "txtIdenMethod": "",
                        "selIdenMethod": "AND",
                        "txtFormula": "",
                        "selFormula": "AND",
                        "txtType": "",
                        "selType": "AND",
                        "txtActivity": "",
                        "selActivity": "AND",
                        "txtIupac": "",
                        "selIupac": "AND",
                        "txtWild": "",
                        "btnSubmit": "Search"}
            payload = 'txtPlantName=Abies+borisii-regis&selPlantName=AND&txtLocation=&selLocation=AND&txtYear=&selYear=AND&txtVolume=&selVolume=AND&txtArticle=&selArticle=AND&txtAuthor=&selAuthor=AND&txtJournal=&selJournal=AND&txtFamily=&selFamily=AND&txtPlantStage=&selPlantStage=AND&txtExpCond=&selExpCond=AND&txtCompoundName=&selCompoundName=AND&txtCas=&selCas=AND&txtPercentage=&selPercentage=AND&txtPlantPart=&selPlantPart=AND&txtIdenMethod=&selIdenMethod=AND&txtFormula=&selFormula=AND&txtType=&selType=AND&txtActivity=&selActivity=AND&txtIupac=&selIupac=AND&txtWild=&btnSubmit=Search'
            #print(payload)
        
            yield Request(link, method = 'POST',  headers= headers,
                          body =payload, meta={'dont_merge_cookies': True},callback= self.parse,
                                                 dont_filter = True) # body= payload,
            
            
        
    def parse(self, response):
        print('rgrgb------------------------------------------------------------------------------------')
        print(response.text)

        pass
