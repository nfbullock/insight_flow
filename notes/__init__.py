import os
from datetime import datetime
import pytz

import config


def _get_modified_files():
    now_pacific = datetime.now(pytz.timezone(config.timezone))
    start_of_day_pacific = now_pacific.replace(hour=0, minute=0, second=0, microsecond=0)
    files_modified_today = []
    for dirpath, dirnames, filenames in os.walk(config.notes_directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if any(i in file_path for i in config.notes_ignored_directories):
                continue
            timestamp = os.path.getmtime(file_path)
            dt = datetime.fromtimestamp(timestamp, tz=pytz.timezone('US/Pacific'))
            if dt > start_of_day_pacific:
                file_path = file_path.replace(config.notes_directory, "")
                file_path = file_path.replace(".md", "").strip("/")
                readable_title = "-".join(file_path.split("/"))
                files_modified_today.append(readable_title)
    return files_modified_today


def review():
    return {"files_modified_today": _get_modified_files()}


if __name__ == "__main__":
    print(_get_modified_files())