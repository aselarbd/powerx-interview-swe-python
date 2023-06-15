from datetime import datetime
from db import timestamp_records_in_database, get_reading
from server.api.utils import Metrics


def _get_timestamps_between_period(from_timestamp=None, to_timestamp=None) -> list:
    # TODO filter records based on from and to values

    # Thought approach :
    #   1. sort timestamp_records_in_database
    #   2. do a binary search for each end (front and back)
    #   3. filter timestamps

    return timestamp_records_in_database


def get_data_service(from_timestamp: str = None, to_timestamp: str = None) -> tuple[list, int]:
    timestamps = _get_timestamps_between_period(from_timestamp=from_timestamp, to_timestamp=to_timestamp)
    result = []

    for timestamp in timestamps:
        reading = get_reading(key=str(timestamp))

        dt_timestamp = datetime.fromtimestamp(timestamp)
        iso_datetime_string = dt_timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        if reading.current:
            result.append({'time': iso_datetime_string, 'name': Metrics.CURRENT.value, 'value': reading.current})
        if reading.voltage:
            result.append({'time': iso_datetime_string, 'name': Metrics.VOLTAGE.value, 'value': reading.voltage})

    # TODO: do power calculation for each day in timestamps

    # Thought approach :
    #   1. filter timestamps based on each day
    #   2. for each day calculate power and add to result array

    return result, 200
