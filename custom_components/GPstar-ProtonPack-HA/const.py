"""Constants for integration_blueprint."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "GPstar-ProtonPack-HA"
DOMAIN = "GPstar-ProtonPack-HA"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by http://jsonplaceholder.typicode.com/"


# Sensors

SENSOR_KEY = "key"
SENSOR_ATTRS = "attrs"
SENSOR_CATEGORY = "cat"
SENSOR_UNIT = "unit"


SENSORS = {
    "battVoltage": dict(
        [
            (SENSOR_KEY, "battVoltage"),
        ]
    ),
    "Ribbon Cable": dict(
        [
            (SENSOR_KEY, "cable"),
        ]
    ),
    "Cyclotron": dict(
        [
            (SENSOR_KEY, "cyclotron"),
        ]
    ),
}