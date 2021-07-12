"""
Created on Mon May  3 01:35:16 2021

@author: ADMJLA
"""

import re

clean1 = ""

# opening and reading the file
with open("/var/lib/elasticip/src/IP.yml") as fh:
   fstring = fh.readlines()
#print ("declaring IPs")
# decalring regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})')
 
# initializing lst
lst=[]

# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])
 
clean1 = ''.join(lst)

print ("marker")
print(clean1)



output = open("IPclean.yml", "w")
output.write(clean1)
output.close()

#info:
#####################################___________NGINX_______________#######################################

fin = open("/var/lib/elasticip/mnt/lb.yml", "rt")
#output file to write the result to
fout = open("/var/lib/elasticip/src/nginx.conf", "wt")
#for each line in the input file
for line in fin:
        #read replace the string and write to output file
        fout.write(line.replace('ELASTICIP', clean1))
#close input and output files
fin.close()
fout.close()
