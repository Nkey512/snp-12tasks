from datetime import datetime, timedelta


def date_in_future(days):
    now = datetime.now()

    if not isinstance(days, int):
        return now.strftime("%d-%m-%Y %H:%M:%S")

    delta = timedelta(days=days)
    future = now + delta
    return future.strftime("%d-%m-%Y %H:%M:%S")
