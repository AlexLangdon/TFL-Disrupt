import requests
import time
import atexit
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

class query_tfl_obj():
    query_rate = 10
    last_query_time = time.time()
    logging.basicConfig()

    def start_tfl_query_loop(self) :
        scheduler = BackgroundScheduler()
        scheduler.start()
        scheduler.add_job(
            func=self.query_tfl,
            trigger=IntervalTrigger(seconds=self.query_rate),
            id='TFL_Status_Job',
            name='Query TFL every '+str(self.query_rate)+' seconds',
            replace_existing=True)
        # Shut down the scheduler when exiting the app
        atexit.register(lambda: scheduler.shutdown())

    def query_tfl(self) :
        res = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=False')
        print res.json()

        time_now = time.time()
        time_delta = time.time() - self.last_query_time
        print 'Time Delta = ' + str(time_delta)
        self.last_query_time = time_now

    def main(self) :
        self.start_tfl_query_loop()
'''
statuses = json[i]["lineStatuses"]
line_id = json[i]["id"]
severity_text = statuses["statusSeverity"]
line_db_entry = db_obj[line_id]
severity_text_stored = line_db_entry["statusText"]
if(severity_text != severity_text_stored) :
    dbObj[line_id] = severity_text
    phone_nums = line_db_entry["nums"]
    sms_out.sms_out(statusText,phone_nums)
'''