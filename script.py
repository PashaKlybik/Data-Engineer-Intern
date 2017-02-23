import csv
from bs4 import BeautifulSoup
import urllib3
import argparse



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
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("File")
	args = parser.parse_args()
	wiki_urls = [["wikipedia_page_url", "website_url"]]
	with open(args.File,'r') as read:
		reader = csv.reader(read)
		for row in reader:
			wiki_urls.append(row)

	for id in range(1, len(wiki_urls)):
		temp = find_url(wiki_urls[id][0])
		wiki_urls[id].append(temp)

	with open("wikipedia_answers.csv", "w") as out_file:
		writer = csv.writer(out_file)
		writer.writerows(wiki_urls)
 