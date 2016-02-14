from quora import quora
from wunderlist.wunderlist_downloader import Wunderlist

class Stats:
	quora_answers = 0
	wunderlist_tasks = 0

	def __init__(self):
		self.refresh()

	def refresh(self):
		self.quora_answers = quora.num_answers()

		#w = Wunderlist()
		#self.wunderlist_tasks = w.get_college_tasks()