"""
Created on Sat May  1 14:15:16 2021

@author: ADMJLA
"""
import re

clean1 = ""


with open("/var/lib/elasticip/src/result.yml") as fh:  
   fstring = fh.readlines()
print ("declaring IP")
print (fstring)
# decalring the regex pattern for IP addresses
pattern = re.compile(r'"(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})"')
 
# initializing the list object
lst=[]

# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
 
# displaying the extracted IP adresses


clean1 = ''.join(lst)



output = open("/var/lib/elasticip/src/IP.yml", "wt")
output.write(clean1)
output.close()
