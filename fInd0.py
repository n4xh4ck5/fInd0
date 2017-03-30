import requests
from urlparse import urlparse
from bs4 import BeautifulSoup
import argparse
from argparse import RawTextHelpFormatter
from pprint import pprint
import json
######FUNCTION EXPORT RESULTS #######
def ExportResults(data):
	#Export the results in json format
	with open ('output.json','w') as f:
		json.dump(data,f)
parser = argparse.ArgumentParser(description='This script searchs domains and subdomains about a domain using the results indexed of Bing search', formatter_class=RawTextHelpFormatter)
parser.add_argument('-t','--target', help="The keyword which it wants to search",required=True)
parser.add_argument('-l','--language', help='Indicate the language of the search\n\n\t(es)-Spanish(default)\n\t(en)-English', required=False)
args = parser.parse_args()
print "  __ _____           _  ___"  
print " / _|_   _|         | |/ _ \ "
print "| |_  | |  _ __   __| | | | |"
print "|  _| | | | '_ \ / _` | | | |"
print "| |  _| |_| | | | (_| | |_| |"
print "|_| |_____|_| |_|\__,_|\___/ "
print "\n"
print """** Tool to get domains in sold about a target
		 ** Author: Ignacio Brihuega Rodriguez a.k.a N4xh4ck5
		 ** DISCLAMER This tool was developed for educational goals. 
		 ** The author is not responsible for using to others goals.
		 **  A high power, carries a high responsibility!"""         
target=args.target
language=args.language
if language is None:
	language="es"
if ((language != "es") and (language !="en")):
	print "The language is not valid"
	exit(1)
url="https://sedo.com/service/common.php?safe_search=2&synonyms=true&number_of_words_min=1&number_of_words_max=0&len_min=1&len_max=0&special_characters%5B%5D=3&special_characters%5B%5D=1&special_characters%5B%5D=2&cat%5B%5D=0&cat%5B%5D=0&cat%5B%5D=0&type=0&special_inventory=4&kws=contains&age_min=0&age_max=0&keyword="+target+"&page=1&rel=6&orderdirection=2&domainIds=&cc=&member=&v=0.1&o=json&m=search&f=requestSearch&pagesize=100&keywords_join=AND&language="+language
response=requests.get(url)
content=response.text
data = json.loads(content)
#parser HTMLt
newlist=[]
print "Domains in buy/sold of "+target+" are:\n"
for x in data['b']['general']['searchRequest']['resultList']:
	if x != None:
		print x['0']
		newlist.append(x['0'])
	ExportResults(newlist)
