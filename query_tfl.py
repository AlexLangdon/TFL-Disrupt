import requests
import time
import atexit
import logging
import json
import sms_out

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from db import db_obj

class query_tfl_obj():
    query_rate = 10
    last_query_time = time.time()
    db_obj = db_obj()
    sms_out_obj = sms_out.sms_out_obj()

    def send_status(self,phone_num,line_id) :
        line_db_entry = db_obj.db_store[line_id]
        severity_text_stored = line_db_entry["status_text"]
        self.sms_out_obj.send_sms(line_id + " line status : " +severity_text_stored, [phone_num])

    def get_status(self, line_id):
        line_db_entry = db_obj.db_store[line_id]
        severity_text_stored = line_db_entry["status_text"]
        return line_id + " line status : " +severity_text_stored

    #NEED TO SPLIT THIS FUNCTION UP INTO SUB FUNCTIONS
    def parse_tfl_json(self, tfl_json) :
        tfl_py_obj = tfl_json

        for line_obj in tfl_py_obj :
            statuses = line_obj["lineStatuses"]
            line_id = line_obj["id"]
            severity_text = statuses[0]["statusSeverityDescription"]

            if "reason" in statuses[0] :
                severity_text += " - "+statuses[0]['reason']

            line_db_entry = db_obj.db_store[line_id]
            severity_text_stored = line_db_entry["status_text"]

            # print "Stored "+severity_text_stored
            # print "Now "+severity_text

            if severity_text != severity_text_stored :
                line_db_entry["status_text"] = severity_text
                sms_text = "Update on "+ line_id + " line : "+severity_text
                phone_nums = line_db_entry["nums"]
                self.sms_out_obj.send_sms(sms_text, phone_nums)

    def query_tfl(self) :
        res = requests.get('https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=False')
        print res.json()
        self.parse_tfl_json(res.json())

        time_now = time.time()
        time_delta = time.time() - self.last_query_time
        print 'Time Delta = ' + str(time_delta)
        self.last_query_time = time_now

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

    def main(self, debug = True) :
        if not debug :
            logging.basicConfig()
        self.start_tfl_query_loop()
