import datetime
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date | datetime.datetime):
            return obj.isoformat(sep=' ', timespec='seconds')
        if isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat(sep=' ', timespec='seconds')

        return json.JSONEncoder.default(self, obj)
