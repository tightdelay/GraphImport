import urllib2,urllib, io, gzip

import time,lxml.html
from datetime import datetime, timedelta

####kleiner Trick, da nicht tagesaktuell:

Today = datetime.today() - timedelta(30)
Today = Today.strftime("%Y%m%d")
print Today

Datum = Today


#print time.strftime("%Y%m%d")
#Datum=time.strftime("%Y%m%d")



############# Extract File List
connection = urllib2.urlopen('http://data.caida.org/datasets/topology/ark/ipv4/as-links/team-1/2017/')
Liste = []

dom =  lxml.html.fromstring(connection.read())

for link in dom.xpath('//a/@href'): # select the url in href for all a tags(links)
    Liste.append("http://data.caida.org/datasets/topology/ark/ipv4/as-links/team-1/2017/" + str(link))
#############
#print Liste

connection.close()

#matching = [s for s in Liste if Datum in s]
#print matching
matching = [i for i ,x in enumerate(Liste) if Datum in x]
print Liste[matching[0]]
URL = Liste[matching[0]]
print URL, type(URL)
############ END: Extract File List
#Datum=int(Datum)-30
#print Datum


response = urllib.urlopen(URL)
compressed_file = io.BytesIO(response.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)

Filename= "PYDL"+ Datum + ".txt"
print Filename

with open(Filename, 'wb') as outfile:
    outfile.write(decompressed_file.read()) 
