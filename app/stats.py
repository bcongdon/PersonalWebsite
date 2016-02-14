from quora import quora
from wunderlist.wunderlist_downloader import Wunderlist

class Stats():
	quora_answers = None
	wunderlist_tasks = None

	def __init__(self):
		pass

	def refresh(self):
		self.quora_answers = quora.num_answers()
		w = Wunderlist()
		self.wunderlist_tasks = w.get_college_tasks()

s = Stats()
s.refresh()
print s.wunderlist_tasks