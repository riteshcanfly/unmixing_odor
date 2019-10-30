import json

class writing:
    
    def write(self,compound):
    	
    	f = open("essentialoil_data.json", "a+")
    	f.write(json.dumps(compound))
    	f.write('\n')
    	f.close()


obj3=writing()
