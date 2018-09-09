import json
import httplib2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)



estados=("H","kh","Mh","GH","TH","PH")
h = httplib2.Http(".cache")

# API ETH
resp, content = h.request("https://www.etherchain.org/api/basic_stats", "GET")
#resp, content = h.request("https://api.akroma.io/network", "GET")
cadena_content ="[" + content.decode("ASCII") +"]"
#print (cadena_content)
todos = json.loads(cadena_content)
hashrate = todos[0]["currentStats"]["hashrate"]
i=0
while (len(str(int(hashrate)))>3):
    #print (len(str(int(hashrate))))
    hashrate=hashrate/1000
    i=i+1
print ("Ethereum Hashrate:",hashrate , estados[i])



# API AKROMA
resp, content = h.request("https://api.akroma.io/network", "GET")
cadena_content ="[" + content.decode("ASCII") +"]"
#print (cadena_content)
todos = json.loads(cadena_content)
hashrate_str = todos[0]["hashRate"]
hashrate_str=hashrate_str.replace(".","")
hashrate=int(hashrate_str)
i=2
while (len(str(int(hashrate)))>3):
    #print (len(str(int(hashrate))))
    hashrate=hashrate/1000
    i=i+1
print ("Akroma Hashrate:",hashrate , estados[i])
