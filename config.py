from typing import Dict, List

import yaml
import datetime

DEFAULT_CONFIG = "config.yml"
SOURCES_NODE = "sources"
OUTPUTFILE_NODE = "outputfile"
DATE_TAG = "{date}"
DATE_FORMAT = "%Y-%m-%d"

class Config:
    def __init__(self, config_file: str = DEFAULT_CONFIG) -> None:
        self._config = self._read_config(config_file)

    def _read_config(self, file_path) -> dict:
        with open(file_path, "r") as f:
            return yaml.safe_load(f)

    @property
    def list(self) -> list:
        return self._config[SOURCES_NODE]

    @property
    def today(self) -> str:
        return datetime.datetime.now().strftime(DATE_FORMAT)

    @property
    def outputfile(self) -> str:
        return self._config[OUTPUTFILE_NODE].replace(DATE_TAG, self.today)
