import wunderpy2
import csv
import json
import datetime
import sys

def main():
    #Define standard date format
    date_format = "%Y-%m-%d"

    #Initialize Wunderpy2 API
    api = wunderpy2.WunderApi()

    #Open auth file and initialize client
    try:
        with open("wunderlist_auth.json","r") as f:
            js = json.loads(f.read())
            access_token = js['access_token']
            client_id = js['client_id']
            personal_id = None
            if 'personal_id' in js.keys():
                personal_id = js['personal_id']
    except Exception as e:
        print e
        print "ERROR: Perhaps you didn't rename \"wunderlist_auth_sample.json\" to \"wunderlist_auth.json\"?"
        sys.exit(0)
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

    min_date = datetime.datetime(year=2015, month=8, day=20)
    print len([f for f in all_completed_tasks if datetime.datetime.strptime(f['completed_at'][:10],date_format) > min_date])
    # #Setup CSV file
    # with open('output.csv','wb') as csvfile:
    #     #Setup CSV writer
    #     csv_writer = csv.writer(csvfile,dialect='excel')

    #     #Write title row
    #     csv_writer.writerow(['Date','Total'] + [_list['title'] for _list in wunderlists])
    #     d = min_date
    #     delta = datetime.timedelta(days=1)
    #     while d <= max_date:
    #         #Format the datetime to readable string
    #         d_str = d.date().strftime(date_format)

    #         list_subtotals = [len([x for x in _list if x['completed_at'][:10] == d_str]) for _list in list_tasks]

    #         #Write the row for specific day column
    #         csv_writer.writerow([d_str,len([x for x in all_completed_tasks if x['completed_at'][:10] == d_str])]
    #             + list_subtotals)

    #         #Iterate current date by 1 day
    #         d+= delta
if __name__ == "__main__":
    main()