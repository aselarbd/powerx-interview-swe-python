from db import timestamp_records_in_database, Reading, add_reading, get_reading
from server.api.add_data.validator import Validator
from server.api.utils import Metrics


def add_data_service(plaintext_data: str) -> tuple[dict, int]:

    try:
        for raw_data in plaintext_data.split('\n'):

            timestamp, metric_name, metric_value = raw_data.split(' ')
            raw_record = {'timestamp': timestamp, 'metric_name': metric_name, 'metric_value': metric_value}
            validated_record = Validator(**raw_record)

            voltage = float(validated_record.metric_value) if validated_record.metric_name == Metrics.VOLTAGE.value else None
            current = float(validated_record.metric_value) if validated_record.metric_name == Metrics.CURRENT.value else None
            metric_timestamp = int(validated_record.timestamp)

            if metric_timestamp not in timestamp_records_in_database:

                reading = Reading(timestamp=metric_timestamp, voltage=voltage, current=current)
                add_reading(key=str(metric_timestamp), reading=reading)
                timestamp_records_in_database.append(metric_timestamp)

            else:

                reading = get_reading(key=str(metric_timestamp))
                if voltage:
                    reading.voltage = voltage
                else:
                    reading.current = current

    except ValueError:
        return {"success": False}, 400

    return {"success": True}, 201
