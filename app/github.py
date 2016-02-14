from bs4 import BeautifulSoup
import requests

def num_commits():
	response = requests.get("https://github.com/benjamincongdon")
	soup = BeautifulSoup(response.content, 'html.parser')
	num_commits = soup.find_all("span",class_="contrib-number")[0].get_text().split()[0]
	return num_commits