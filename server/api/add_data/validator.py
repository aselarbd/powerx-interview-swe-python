from pydantic import BaseModel, validator
from server.api.utils import Metrics


class Validator(BaseModel):
    timestamp: str
    metric_name: str
    metric_value: str

    @validator('timestamp')
    def validate_timestamp(cls, value):
        if not value.isdigit():
            raise ValueError("Invalid timestamp.")
        return value

    @validator('metric_name')
    def validate_metric_name(cls, value):
        if value not in (Metrics.VOLTAGE.value, Metrics.CURRENT.value):
            raise ValueError("Invalid metric name.")
        return value

    @validator('metric_value')
    def validate_metric_value(cls, value):
        try:
             val = float(value)
        except ValueError:
            raise ValueError("Invalid metric value.")
        return val
