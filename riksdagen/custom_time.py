from datetime import datetime

def str_to_datetime(date: str) -> datetime:
    return datetime.strptime(date, '%Y-%m-%d %X')