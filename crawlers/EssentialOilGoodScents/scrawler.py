import bs4 as bs
import urllib.request
import json
import re
import info as c

class scrawler:
    def get_urls(self,alphabet):
        z=0
        alphabetlen = len(alphabet)
        
        while(z<alphabetlen):
                #print(len(alphabet))
                sauce = urllib.request.urlopen(alphabet[z]).read()
                soup=bs.BeautifulSoup(sauce,'html.parser')
                self.urllist=[]

                for tr in soup.find_all('a'):
                        tr1=tr.get('onclick')
                        tr2=re.sub('openMainWindow\(\'','',str(tr1))
                        tr3=re.sub('\'\);return false;','',tr2)
                        self.urllist.append(tr3)
                self.count=0
                print(len(self.urllist))
                while(self.count < len(self.urllist)):
                      obj1.webpage(z)
                      self.count = self.count+1
                z=z+1

    def webpage(self,z):
        print(self.count)

        urlpage=self.urllist[self.count]
        #urlpage=self.urllist[22]
        #urlpage = 'http://www.thegoodscentscompany.com/data/es1067561.html'
        print(urlpage)
        sauce = urllib.request.urlopen(urlpage).read()
        soup = bs.BeautifulSoup(sauce,'html.parser')
        try:
            c.obj2.details(soup)
            #c.obj2.organoleptic_properties(soup,z,self.count)            
            #c.obj2.potential_blenders(soup,z,self.count)
        except Exception as e:
            print(e)
            f=open("leftovers.txt", "a+")
            f.write(str(self.urllist[self.count]))
            f.write('\n')
            f.close()
        
obj1=scrawler()

