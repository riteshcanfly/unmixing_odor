import bs4 as bs
import urllib.request
import json
import re
import scrawler as b

class main:
    def url(self):
        sauce0 = urllib.request.urlopen('http://www.thegoodscentscompany.com/#').read()
        main.soup0=bs.BeautifulSoup(sauce0,'html.parser')
        return obj.alphabets()

    def alphabets(self):
        urllist=[]
        alphabet=[]
        for s in main.soup0.find_all('a'):
            a=s.get('href')
            if 'http://www.thegoodscentscompany.com/ess-' in a:
                alphabet.append(a)
        return alphabet
    
obj=main()
alphabet=obj.url()
#alphabet = alphabet[10:]
print(alphabet)
b.obj1.get_urls(alphabet)






