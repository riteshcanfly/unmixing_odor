import bs4 as bs
import urllib.request
import json
import re
import write as d
from potential import get_potential 

class parsing:
    def details(self,soup):
        self.compound={}
        print('in details')
        cheminfo=soup.find_all('table',class_="cheminfo")
        head=soup.thead.text.split('/n')
        common_name,description=head[0].split('\r\n')
        common_name_filtered=re.sub('\n','',common_name)
        description_filtered=re.sub('\n','',description)
        radw8=cheminfo[0].find_all('td',class_='radw8')

        radw7=cheminfo[0].find_all('td',class_='radw7')
        radw11=cheminfo[0].find_all('td',class_='radw11')
        details={}
        if len(radw8)==0:
            print('no details')
        else:

            if radw8[0].text=='CAS Number: ':
                details[re.sub(': ','',radw8[0].text)]=radw11[0].text
                
            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text

            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ' and radw8[2].text=='FDA UNII: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text
                details[re.sub(': ','',radw8[2].text)]=radw7[1].text
                            
            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ' and radw8[2].text=='FDA UNII: ' and radw8[3].text=='CoE Number: ' and radw8[4].text=='Also Contains: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text
                details[re.sub(': ','',radw8[2].text)]=radw7[1].text
                details[re.sub(': ','',radw8[3].text)]=radw7[2].text
                details[re.sub(': ','',radw8[4].text)]=radw7[3].text
                        
            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ' and radw8[2].text=='Also Contains: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text
                details[re.sub(': ','',radw8[2].text)]=radw7[1].text

            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ' and radw8[2].text=='Other: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text
                details[re.sub(': ','',radw8[2].text)]=radw7[1].text

            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ' and radw8[2].text=='ECHA EC Number: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text
                details[re.sub(': ','',radw8[2].text)]=radw7[1].text

            elif radw8[0].text=='Name: ' and radw8[1].text=='CAS Number: ' and radw8[2].text=='ECHA EC Number: ' and radw8[3].text=='Also Contains: ':
                details[re.sub(': ','',radw8[0].text)]=radw7[0].text
                details[re.sub(': ','',radw8[1].text)]=radw11[0].text
                details[re.sub(': ','',radw8[2].text)]=radw7[1].text
                details[re.sub(': ','',radw8[3].text)]=radw7[2].text


        details["Common Name"]=re.sub('\xa0','',common_name_filtered)
        print(re.sub('\xa0','',common_name_filtered))
        details["Description"]=re.sub('\xa0','',description_filtered)
        self.compound["Details"]=details
        self.physical_properties(soup)
    
    def physical_properties(self,soup):
        
        print('in physical')
        physical={}
        similaritems={}
        soluble=[]
        insoluble=[]
        cheminfo=soup.find_all('table',class_="cheminfo")        
        physical_keydata=cheminfo[2].find_all('td',class_='radw11')
        physical_keys=cheminfo[2].find_all('td',class_='radw4')
        wrd8=cheminfo[2].find_all('td',class_='wrd8')
        wrd10=cheminfo[2].find_all('td',class_='wrd10')
        wrd12=cheminfo[2].find_all('td',class_='wrd12')
        wrd14=cheminfo[2].find_all('td',class_='wrd14')

        key=''
        i=0
        #print( physical_keydata)
        
        while(i<len(physical_keydata)):
            keydup=key
            key=re.sub('\xa0','',physical_keys[i].text)
            item=re.sub('\xa0','',physical_keydata[i].text)
            item=re.sub('\r\n','',item)
            #print('key and item', (key, item))
            if key=='':
                physical[re.sub(': ','',keydup)] = []
            else:
                physical[re.sub(': ','',key)]=item
                i=i+1
                        
            
        #print(wrd8)
        #print('length of wrd8', len(wrd8))    

        while(i<len(wrd8)):

            if i/2==0:
                soluble.append(wrd8[i].text)
            else:
                insoluble.append(wrd8[i].text)
            i=i+1
        i=0
        while(i<len(wrd10)):
            if i/2==0:
                soluble.append(wrd10[i].text)
            else:
                insoluble.append(wrd10[i].text)
            i=i+1
                        
        insoluble=tuple(insoluble)
        soluble=tuple(soluble)
        physical['Soluble']=soluble
        physical['Insoluble']=insoluble

        i=0
        j=0
        physical["Similar Items"]=similaritems
        while(i<len(wrd12)):
            similaritems[j]=wrd12[i].text
            i=i+1
            j=j+1
        i=0
        while(i<len(wrd14)):
            similaritems[j]=wrd14[i].tpext
            i = i+1
            j = j+1
        self.compound["Physical Properties"]=physical
        self.organoleptic_properties(soup)
        
    def organoleptic_properties(self,soup):
        print('in organoleptic')
        organoleptic={}
        cheminfo=soup.find_all('table',class_="cheminfo")
        radw112=cheminfo[3].find_all('td',class_='radw11')
        radw4=cheminfo[3].find_all('td',class_='radw4')

        ############ Odor Type and Flavor type ########################
        
        try:
            qinfr2 = cheminfo[3].find_all('td',class_='qinfr2')
            #print(qinfr2)

        except Exception as e:
            pass
             
        for ele in qinfr2:
            keyValtext = ele.text
            #print("qinfr2:", keyValtext)
            keyVal = keyValtext.split(":")
            key = keyVal[0]
            val = keyVal[1]
            #print("key:val", (key,val))
            organoleptic[key] = val.strip()  

        ############ Odor Type and Flavor type ########################   


        ############ Odor Description and  Taste Description ########################  
        
        rad=cheminfo[3].find_all('a')  
        odor_des = []
        flavor_des = []
        n=0
        
        while(n<len(rad)):
            links= rad[n].get('href')
            if 'odor' in links:
                odor_des.append(rad[n].text)
            elif 'flavor' in links:
                flavor_des.append(rad[n].text)    
        
            radw4=cheminfo[3].find_all('td',class_='radw4')
            n=n+1
        #print("odor description",odor_des)
        #print("flavor description",flavor_des)

        ############ Odor Description and  Taste Description ########################   

        i=0
        key=''
        while(i<len(radw112)):
            
            key=re.sub('\xa0','',radw4[i].text)
            #print(key)

            item=re.sub('\xa0','',radw112[i].text)
            #print(item)

            if key=='':
                print('nothing')
            elif key=='Odor Description: at 100.00%.':
                organoleptic['Odor Description']= odor_des
            elif key == 'Odor Description: at 10.00'+'%'+ 'indipropylene glycol.':
                organoleptic['Odor Description'] = odor_des       
            
            elif key=='Taste Description: ':
                organoleptic['Taste Description']= flavor_des
            
            else:
                organoleptic[re.sub(': ','',key)]= item
            i=i+1
        
        #print("Organoleptic Properties", organoleptic)

        self.compound["Organoleptic Properties"]=organoleptic

        
        self.potential_blenders(soup)
    
    

    def potential_blenders(self,soup):
        
        print('in potential')
        errorCode = 0
        potential = get_potential(soup)
        self.compound["Potential Blenders"]= potential
        #print(self.compound)
        d.obj3.write(self.compound)


obj2=parsing()
