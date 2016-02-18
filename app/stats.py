from quora import quora
import github
import twitter
from wunderlist.wunderlist_downloader import Wunderlist

class Stats:
	quora_answers = 0
	wunderlist_tasks = 0
	github_commits = 0
	tweets = 0

	def __init__(self):
		pass

	def refresh(self):
		self.quora_answers = quora.num_answers()
		self.github_commits = github.num_commits()
		self.tweets = twitter.num_tweets()
		#w = Wunderlist()
		#self.wunderlist_tasks = w.get_college_tasks()