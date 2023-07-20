import os
from datetime import datetime

import pytz

import config

NOW_LOCAL = datetime.now(pytz.timezone(config.timezone))
TODAY = NOW_LOCAL.date().strftime(config.date_str)


def date_is_today(timestamp):
    dt = datetime.strptime(timestamp, config.utc_timestamp)
    utc_dt = pytz.UTC.localize(dt)
    local_dt = utc_dt.astimezone(pytz.timezone(config.timezone))
    now_local = datetime.now(pytz.timezone(config.timezone))
    if local_dt.date() == now_local.date():
        return True
    return False


def get_file_modified_datetime(file_path):
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp, tz=pytz.timezone(config.timezone))


def get_start_of_day_datetime():
    now_local = datetime.now(pytz.timezone(config.timezone))
    return now_local.replace(hour=0, minute=0, second=0, microsecond=0)


def nag_prompt(message):
    input(
        f"{message}, "
        "now is a good time to organize this area.\n"
        "Press ENTER to proceed..."
    )


def write_data(file_name, data):
    with open(file_name, "w") as f:
        json.dump(data, f, sort_keys=True, indent=True)