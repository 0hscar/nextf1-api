import pandas as pd
from datetime import datetime
import fastf1

_cached_schedule = None
_cached_timestamp = None
_CACHE_TTL = pd.Timedelta(days=1)  # Cache TTL of 1 day

def get_schedule():
    global _cached_schedule, _cached_timestamp
    now = datetime.now()

    if _cached_schedule is None or _cached_timestamp is None or now - _cached_timestamp > _CACHE_TTL:
        current_year = now.year
        _cached_schedule = pd.DataFrame(fastf1.get_event_schedule(current_year))
        _cached_timestamp = now
    return _cached_schedule



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
    "Qualifying Date": "Session4Date",
    "Race": "Session5",
    "Race Date": "Session5Date",
}

# Filter the schedule based on the library mapping

# For testing
# custom_time = datetime.now().astimezone() + pd.Timedelta(weeks=3)


def get_next_event():
    current_time = datetime.now().astimezone()
    df = get_schedule()
    upcoming_events = df[df["Session5Date"] > current_time]

    if not upcoming_events.empty:
        # This is a Series representing a single row
        next_upcoming_event = upcoming_events.iloc[0]
        event_details = {}
        for session, session_date in [
            (next_upcoming_event.get("Session1"), "Session1Date"),
            (next_upcoming_event.get("Session2"), "Session2Date"),
            (next_upcoming_event.get("Session3"), "Session3Date"),
            (next_upcoming_event.get("Session4"), "Session4Date"),
            (next_upcoming_event.get("Session5"), "Session5Date"),
        ]:
            session_time = next_upcoming_event.get(session_date)
            if pd.notna(session_time) and isinstance(session_time, pd.Timestamp):
                if session_time > current_time:
                    event_details[session] = {
                        "date": session_time.isoformat(),
                        "time_until_event": str(session_time - current_time),
                        "status": "upcoming",
                        "day": session_time.strftime("%A"),
                    }
                else:
                    event_details[session] = {
                        "date": session_time.isoformat(),
                        "day": session_time.strftime("%A"),
                        "status": "completed",
                    }
        event_details["Country"] = next_upcoming_event["Country"]
        return event_details
    return None
