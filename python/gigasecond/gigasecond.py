from datetime import datetime, timedelta


def add(moment: datetime) -> datetime:
    """Add a gigasecond to a moment."""
    return moment + timedelta(seconds=1_000_000_000)
