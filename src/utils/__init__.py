def fetch_next_event(filtered_schedule):
    current_time = datetime.now().astimezone()
    next_upcoming_event = filtered_schedule[filtered_schedule['Session1Date'] > current_time].iloc[0]
    return next_upcoming_event

def calculate_time_until_event(event_date):
    current_time = datetime.now().astimezone()
    time_until_event = event_date - current_time
    days, remainder = divmod(time_until_event.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)
    return int(days), int(hours), int(minutes)

def format_event_details(session, days, hours, minutes):
    return f"{session}: {days} days, {hours} hours, {minutes} minutes"