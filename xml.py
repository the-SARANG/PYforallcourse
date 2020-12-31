from urllib.request import urlopen
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import ssl

sumup=0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
xml = urlopen(url, context=ctx).read()
soup = BeautifulSoup(xml, "html.parser")

#counting sum of numbers
print('Retrieved', len(xml), 'characters')
x=xml.decode()
tree = ET.fromstring(x)
counts = tree.findall('.//count')
print("Count of Comment:",len(counts))
for count in counts:
    sumup += int(count.text)

print(sumup)
