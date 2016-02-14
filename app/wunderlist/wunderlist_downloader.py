import wunderpy2
import csv
import json
import datetime
import sys
import os

class Wunderlist():
    result = None
    def __init__(self):
        pass
        
    def get_college_tasks(self):
        if self.result == None:
            self.result = self.get_completed_tasks_after(datetime.datetime(year = 2015, month = 8, day = 20))
        return self.result

    def get_completed_tasks_after(self, startdate):
        #Define standard date format
        date_format = "%Y-%m-%d"

        #Initialize Wunderpy2 API
        api = wunderpy2.WunderApi()

        #Open auth file and initialize client
        try:
            path = os.path.join(os.getcwd(),"append","wunderlist","wunderlist_auth.json")
            with open(path,"r") as f:
                js = json.loads(f.read())
                access_token = js['access_token']
                client_id = js['client_id']
                personal_id = None
                if 'personal_id' in js.keys():
                    personal_id = js['personal_id']
        except Exception as e:
            print e
            print "ERROR: Perhaps you didn't rename \"wunderlist_auth_sample.json\" to \"wunderlist_auth.json\"?"
            return 0

        client = api.get_client(access_token, client_id)
        print "** Client Initialized"

        #Pull down all lists
        wunderlists = client.get_lists()
        print "** List of Lists Pulled"

        all_completed_tasks = list()
        list_tasks = list()
        for list_ in wunderlists:
            completed = client.get_tasks(list_['id'], completed=True)
            all_completed_tasks += completed
            list_tasks.append(completed)
            print "Pulled \"" + str(list_['title']) + "\""

        #If personal_id is defined in wunderlist_auth, remove all tasks not completed by that ID
        if personal_id is not None:
            all_completed_tasks = [task for task in all_completed_tasks if 'completed_by_id' in task.keys() and task['completed_by_id'] == personal_id]
            new_list_tasks = list()
            for _list in list_tasks:
                new_list_tasks.append([task for task in _list if 'completed_by_id' in task.keys() and task['completed_by_id'] == personal_id])
            list_tasks = new_list_tasks

        #Sort completed tasks by completion date
        all_completed_tasks = sorted(all_completed_tasks, key=lambda task: task['completed_at'])

        #Strip the completion start/end dates into datetimes
        min_date = datetime.datetime.strptime(all_completed_tasks[0]['completed_at'][:10],date_format)
        max_date = datetime.datetime.strptime(all_completed_tasks[len(all_completed_tasks) - 1]['completed_at'][:10],date_format)

        min_date = startdate
        return len([f for f in all_completed_tasks if datetime.datetime.strptime(f['completed_at'][:10],date_format) > min_date])
