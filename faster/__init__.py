DEFAULT_FAST = "16:8"


def generate(review_metadata: dict):
    return {"type": DEFAULT_FAST, "diet": "ketobiotic"}


def review():
    data = {}
    if bool(input("did you fast today? (y/N): ") or 0):
        data["start"] = input("start time? (24HH:MM)")
        data["end"] = input("end time? (24HH:MM)")
        data["comments"] = input("any comments?")
    return data
