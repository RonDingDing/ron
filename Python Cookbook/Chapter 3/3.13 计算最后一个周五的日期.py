from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(datetime.today()) # For reference
# 2018-10-31 10:58:28.750934
print(get_previous_byday('Monday'))
# 2018-10-29 10:58:28.750934
print(get_previous_byday('Tuesday')) # Previous week, not today
# 2018-10-30 10:58:28.750934
print(get_previous_byday('Friday'))
# 2018-10-26 10:58:28.750934