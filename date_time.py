from datetime import datetime

def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

def get_date():
    today = datetime.now()
    return today.strftime("%B %d, %Y")