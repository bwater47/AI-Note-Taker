from datetime import datetime

def format_date():
    current_date = datetime.now()
    return f"{current_date.month}/{current_date.day}/{current_date.year}"

