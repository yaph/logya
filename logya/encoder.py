# -*- coding: utf-8 -*-
import datetime
import json


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat(sep=' ', timespec='seconds')
        elif isinstance(obj, datetime.date):
            return obj.isoformat(sep=' ', timespec='seconds')
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat(sep=' ', timespec='seconds')

        return json.JSONEncoder.default(self, obj)
