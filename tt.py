import csv
from bs4 import BeautifulSoup
import urllib3


def find_url(url):
	http = urllib3.PoolManager()
	r = http.request('GET', url)
	while r.status !=200:
		r = http.request('GET', url)
	soup = BeautifulSoup(r.data)
	a =soup.find("table", { "class" : "infobox" })
	for i in a.find_all("tr"):
		if  i.find("th", text = "Website")!=None:
			return i.find("a")["href"]
		
def main():	
	wiki_urls = list()
	with open("wikipedia_links.csv",'r') as read:
		reader = csv.reader(read)
		for row in reader:
			wiki_urls.append(row)

	for id in range(len(wiki_urls)):
		temp = find_url(wiki_urls[id][0])
		wiki_urls[id].append(temp)

	with open("wikipedia_answers_example1.csv", "w") as out_file:
		writer = csv.writer(out_file)
		writer.writerows(wiki_urls)