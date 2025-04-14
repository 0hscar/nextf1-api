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
    "Practice 2": "Session2",
    "Practice 2 Date": "Session2Date",
    "Sprint Qualifying": "Session2",
    "Sprint Qualifying Date": "Session2Date",
    "Practice 3": "Session3",
    "Practice 3 Date": "Session3Date",
    "Sprint": "Session3",
    "Sprint Date": "Session3Date",
    "Qualifying": "Session4",
    "Qialifying Date": "Session4Date",
    "Race": "Session5",
    "Race Date": "Session5Date",
}

# Filter the schedule based on the library mapping
filtered_schedule = df[library.values()]

# For testing
custom_time = datetime.now().astimezone() + pd.Timedelta(weeks=3)


def get_next_event():
    current_time = datetime.now().astimezone()

    # TESTING
    # upcoming_events = df[df["Session5Date"] > custom_time]
    
    upcoming_events = df[df["Session5Date"] > current_time]

    if not upcoming_events.empty:
        next_upcoming_event = upcoming_events.iloc[0]
        event_details = {} 
        for session, session_date in [
            (next_upcoming_event["Session1"], "Session1Date"),
            (next_upcoming_event["Session2"], "Session2Date"),
            (next_upcoming_event["Session3"], "Session3Date"),
            (next_upcoming_event["Session4"], "Session4Date"),
            (next_upcoming_event["Session5"], "Session5Date"),
        ]:
            if pd.notna(next_upcoming_event[session_date]):
                # # Add the session country
                if next_upcoming_event[session_date] > current_time:
                    event_details[session] = {
                        "date": next_upcoming_event[session_date].isoformat(),
                        "time_until_event": str(next_upcoming_event[session_date] - current_time),
                        "status": "upcoming",
                        "day": next_upcoming_event[session_date].strftime("%A"),
                    }
                else:
                    event_details[session] = {
                        "date": next_upcoming_event[session_date].isoformat(),
                        "day": next_upcoming_event[session_date].strftime("%A"),
                        "status": "completed",
                    }
        # Add the event name and season
        event_details["Country"] = next_upcoming_event["Country"] 
        return event_details
    return None
