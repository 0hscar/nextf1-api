import pandas as pd
from datetime import datetime
import fastf1

# Fetch the event schedule
current_year = datetime.now().year
df = pd.DataFrame(fastf1.get_event_schedule(current_year))

# Define the mapping for session names
library = {
    "Country": "Country",
    "Practice 1": "Session1",
    "P1 Date": "Session1Date",
    "Sprint Qualifying": "Session2",
    "Sprint Qualifying Date": "Session2Date",
    "Sprint": "Session3",
    "Sprint Date": "Session3Date",
    "Qualifying": "Session4",
    "Qialifying Date": "Session4Date",
    "Race": "Session5",
    "Race Date": "Session5Date",
}

# Filter the schedule based on the library mapping
filtered_schedule = df[library.values()]

def get_next_event():
    current_time = datetime.now().astimezone()
    upcoming_events = filtered_schedule[filtered_schedule["Session5Date"] > current_time]

    if not upcoming_events.empty:
        next_upcoming_event = upcoming_events.iloc[0]
        event_details = {}
        for session, session_date in [
            ("Session1", "Session1Date"),
            ("Session2", "Session2Date"),
            ("Session3", "Session3Date"),
            ("Session4", "Session4Date"),
            ("Session5", "Session5Date"),
        ]:
            if pd.notna(next_upcoming_event[session_date]):
                if next_upcoming_event[session_date] > current_time:
                    event_details[session] = {
                        "date": next_upcoming_event[session_date].isoformat(),
                        "time_until_event": str(next_upcoming_event[session_date] - current_time),
                        "status": "upcoming",
                    }
                else:
                    event_details[session] = {
                        "date": next_upcoming_event[session_date].isoformat(),
                        "status": "completed",
                    }
        print(type(event_details))
        return event_details
    return None