"""Configuration for Card classic."""
import datetime

import yaml

DEFAULT_CONFIG = "config.yml"
SOURCES_NODE = "sources"
OUTPUTFILE_NODE = "outputfile"
DATE_TAG = "{date}"
DATE_FORMAT = "%Y-%m-%d"


class Config:
    """Configuration class?"""

    def __init__(self, config_file: str = DEFAULT_CONFIG) -> None:
        self._config = self._read_config(config_file)

    @staticmethod
    def _read_config(file_path) -> dict:
        """Loads the Configuration file."""
        with open(file_path, "r") as file:
            return yaml.safe_load(file)

    @property
    def list(self) -> list:
        """Returns the sources as a list of dictionaries."""
        return self._config[SOURCES_NODE]

    @property
    def today(self) -> str:
        """Returns today's date for use in the filename and on the csv file."""
        return datetime.datetime.now().strftime(DATE_FORMAT)

    @property
    def outputfile(self) -> str:
        """Returns the path of the output file."""
        return self._config[OUTPUTFILE_NODE].replace(DATE_TAG, self.today)
