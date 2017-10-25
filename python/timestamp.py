import re
import datetime

class Timestamp:
    def __init__(self, d):
        r = re.search('(\d{4})-(\d{2})-(\d{2})T(\d{1,2}):(\d{2}):(\d{2})([+|-])(\d{2}):\d{2}', d)
        offset = datetime.timezone(datetime.timedelta(0,0,0,0,0,int("{}{}".format(r.group(7), r.group(8))),0))
        self.date = datetime.datetime(int(r.group(1)), int(r.group(2)), int(r.group(3)), int(r.group(4)),
                                       int(r.group(5)), int(r.group(6)), 0, offset)

    def date(self):
        return self.date
