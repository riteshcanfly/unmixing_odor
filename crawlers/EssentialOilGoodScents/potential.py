import bs4 as bs
import urllib.request
import json
import re
import os
import csv



class AutoVivification(dict):
	def __getitem__(self, item):
		try:
			return dict.__getitem__(self, item)
		except KeyError:
			value = self[item] = type(self)()
			return value

def display(elements):
	for ele in elements:
		print(ele.text)

def getName_CAS(url):
	Name = None
	CAS = None
	
	try:
		print("opening url: ", url)
		sauce = urllib.request.urlopen(url).read()
	except Exception as e:
		print(e)
		return Name, CAS

	soup=bs.BeautifulSoup(sauce,'html.parser')
	cheminfo = soup.find_all('table',class_="cheminfo")
	radw8 = cheminfo[0].find_all('td',class_='radw8')
	radw7 = cheminfo[0].find_all('td',class_='radw7')
	radw11 = cheminfo[0].find_all('td',class_='radw11')
	head=soup.thead.text.split('/n')
	
	
	try:
		common_name,description=head[0].split('\r\n')
	except:
		common_name = head[0].split('\r\n')

	if common_name == ['\n\xa0\nscotch pine wood']:
		Name = 'scotch pine wood/needles resinoid'
	else:
		common_name = re.sub('\n','',common_name)
		common_name = re.sub('\xa0','',common_name )
	
	
	for ele in radw8:
		if ele.text == 'CAS Number: ':
			CAS = radw11[0].text        
		elif ele.text == 'Name: ' :
			Name = radw7[0].text        
		else:
			continue
	if Name == None:
		Name = common_name

	#print('Name:', Name )
	#print('CAS:', CAS)
	return Name, CAS




def get_potential(soup):

	#sauce = urllib.request.urlopen('http://www.thegoodscentscompany.com/data/es1067561.html').read()
	#soup = bs.BeautifulSoup(sauce,'html.parser')
	print("inside get_potential")
	cheminfo = soup.find_all('table',class_="cheminfo")
	all_text = cheminfo[11].find_all('td')
	main_keys  = cheminfo[11].find_all('td', class_ = 'demstrafrm')
	odor_class  = cheminfo[11].find_all('td', class_ = 'radw46')

	odor_classes = cheminfo[11].findAll(True, {'class':['demstrafrm','radw46', 'wrd89']})

	odor_dict = AutoVivification()


	Namelist = []
	CASlist = []
	entryFlag  = 0
	sec_key = ''
	main_key  = ''
	k = 0

	for ele in odor_classes:
		prev_seckey = sec_key
		prev_mainkey = main_key
		k = k+1
		if k == len(odor_classes):
			#print("in last item")

			link = ele.find('a')
			url = link.get('href')
			Name, CAS = getName_CAS(url)
			#print("last item sec_key", sec_key)
			Namelist.append(Name)
			CASlist.append(CAS)
			odor_dict[main_key][sec_key]['Name'] = Namelist
			odor_dict[main_key][sec_key]['CAS'] = CASlist
			break
		if (ele['class'][0] == 'demstrafrm'):
			main_key = ele.text

			if Namelist or CASlist:
				#print("prev main_key", prev_mainkey)
				odor_dict[prev_mainkey][prev_seckey]['Name'] = Namelist
				odor_dict[prev_mainkey][prev_seckey]['CAS'] = CASlist
				Namelist = []
				CASlist = []
				sec_key = ''
				entryFlag = 0

			continue

		elif (ele['class'][0] == 'radw46'):
			sec_key = ele.text
			#print("sec_key", sec_key)
			if not entryFlag  :
				entryFlag = 1
			else:
				odor_dict[main_key][prev_seckey]['Name'] = Namelist
				odor_dict[main_key][prev_seckey]['CAS'] = CASlist
				#print("odor_dict", odor_dict)
				Namelist = []
				CASlist = []
				pass

			continue

		elif (ele['class'][0] == 'wrd89'):
			link = ele.find('a')
			url = link.get('href')
			Name, CAS = getName_CAS(url)
			Namelist.append(Name)
			CASlist.append(CAS)
			continue
	
	print(odor_dict)		
	return odor_dict
def main():
	url = 'http://www.thegoodscentscompany.com/data/es1067561.html'
	sauce = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(sauce,'html.parser') 
	get_potential(soup)

if __name__ == '__main__':
	main() # test it
	
    