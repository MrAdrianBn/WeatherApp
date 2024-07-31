from datetime import timedelta, datetime, timezone


class TimeFormatter:

    def __init__(self):
        self.local_time = None

    def get_local_time(self):
        return self.local_time

    def set_local_time(self, time_zone):
        temp = int(time_zone) / 3600  # hours
        now_gmt = datetime.now(timezone.utc)
        print(now_gmt)
        self.local_time = now_gmt + timedelta(hours=temp)
