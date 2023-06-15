class Reading:

    def __init__(self, timestamp: int, voltage: float = None, current: float = None) -> None:
        self.timestamp = timestamp
        self.voltage = voltage
        self.current = current


# This is a fake database which stores data in-memory while the process is running
# Feel free to change the data structure to anything else you would like
database: dict[str, Reading] = {}
timestamp_records_in_database = []


def add_reading(key: str, reading: Reading) -> None:
    """
    Store a reading in the database using the given key
    """
    database[key] = reading


def get_reading(key: str) -> Reading | None:
    """
    Retrieve a reading from the database using the given key
    """
    return database.get(key)
