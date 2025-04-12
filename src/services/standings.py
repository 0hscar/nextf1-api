from fastf1.ergast import Ergast
import pandas as pd
ergast = Ergast()

def get_driver_standings():
    """
    Fetch the driver standings from the Ergast API.
    """
    
    try:
        # Fetch the driver standings
        standings = ergast.get_driver_standings(season=2025)
        # Convert to dictionary format
        # standings_list = {}
        print("Get driver standings")
        df = standings.content[0]  # This is an ErgastResultFrame, DataFrame-like
        standings_list = []

        for _, row in df.iterrows():
            driver_name = f"{row['givenName']} {row['familyName']}"
            constructor = row['constructorNames']
            if isinstance(constructor, list):
                constructor = constructor[0] if constructor else "N/A"

            standings_list.append({
                "Driver": driver_name,
                "Constructor": constructor,
                "Points": int(row['points']),
                "Position": int(row['position']),
                "Wins": int(row['wins']),
            })

        return standings_list
    except Exception as e:
        print(f"Error fetching driver standings: {e}")
        return None
    

def get_constructor_standings():
    """
    Fetch the constructor standings from the Ergast API.
    """
    try:
        standings = ergast.get_constructor_standings(season=2025)
        print("Get constructor standings")
        df = standings.content[0]  # This is an ErgastResultFrame, DataFrame-like
        standings_list = []

        for _, row in df.iterrows():
            constructor_name = row['constructorName']
            standings_list.append({
                "Constructor": constructor_name,
                "Points": int(row['points']),
                "Position": int(row['position']),
                "Wins": int(row['wins']),
            })
        return standings_list
    except Exception as e:
        print(f"Error fetching constructor standings: {e}")
        return None

