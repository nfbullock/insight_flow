from datetime import datetime
import pytz

import requests

from . import models
import secrets
import config
import utilities

SYNC_API = "https://api.todoist.com/sync/v9"
REST_API = "https://api.todoist.com/rest/v2"


def _request(url, method, params: dict = None, data: dict = None):
    result = getattr(requests, method)(
        url,
        params=params,
        headers={"Authorization": f"Bearer {secrets.TODOIST_API_TOKEN}"},
        json=data,
    )
    result.raise_for_status()
    return result.json()


def _compare_dates(timestamp):
    timestamp = datetime.strptime(timestamp, config.utc_timestamp)
    utc_dt = pytz.UTC.localize(timestamp)
    pacific_dt = utc_dt.astimezone(pytz.timezone(config.timezone))
    now_pacific = datetime.now(pytz.timezone(config.timezone))
    if pacific_dt.date() == now_pacific.date():
        return True
    return False


def _get_active(dump: bool = True):
    data = []
    results = _request(
        f"{REST_API}/tasks", "get", params={"filter": "overdue | today"}
    )
    for row in results:
        task = models.ActiveTask(**row)
        if dump:
            task = task.dict()
        data.append(task)
    return data


def _get_completed():
    matches = []
    result = _request(
        f"{SYNC_API}/activity/get", "get", params={"event_type": "completed"}
    )
    for event in result["events"]:
        if _compare_dates(event["event_date"]):
            matches.append(event["extra_data"]["content"])
    return matches


def generate():
    return _get_active()


def quick_add():
    text = input("input: ")
    _request(f"{REST_API}/tasks", "post", data={"content": text})


def review():
    utilities.nag_prompt("Todoist review")
    return {
        "active": _get_active(),
        "completed": _get_completed(),
    }


if __name__ == "__main__":
    print(review())
