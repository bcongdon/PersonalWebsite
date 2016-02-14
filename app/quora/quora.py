from bs4 import BeautifulSoup
import requests

def num_answers():
	response = requests.get("https://www.quora.com/profile/Benjamin-Congdon-1")
	soup = BeautifulSoup(response.content, 'html.parser')
	num_answers = soup.find_all("span",class_="list_count")[0].get_text()
	return num_answers