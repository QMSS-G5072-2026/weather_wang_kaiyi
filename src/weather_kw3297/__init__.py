# read version from installed package
from importlib.metadata import version
__version__ = version("weather_kw3297")

from .weather_kw3297 import (
    celsius_to_fahrenheit,
    summarize_temperatures,
    clean_readings,
)
