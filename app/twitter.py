from bs4 import BeautifulSoup
import requests

def num_tweets():
	response = requests.get("https://twitter.com/BenRCongdon")
	soup = BeautifulSoup(response.content, 'html.parser')
	num_tweets = soup.find_all("span",class_="ProfileNav-value")[0].get_text()
	return num_tweets