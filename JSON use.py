import json
from urllib.request import urlopen
import ssl

sumup=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#Taking Input
url = input('Enter - ')
data = urlopen(url, context=ctx).read()
#Retrieving Characters
print('Retrieved', len(data), 'characters')
info=json.loads(data)
print('User count:', len(info))
c=0
for word in info["comments"]:
    cont = int(word['count'])
    sumup+=cont
    c+=1
print("Number of Comments:",c)
print(sumup)
    
    
    




