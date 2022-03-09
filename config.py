from typing import Dict, List

import yaml
import datetime

DEFAULT_CONFIG = 'config.yml'


class Config():

    def __init__(self, config_file: str = DEFAULT_CONFIG) -> None:
        self._config = self._read_config(config_file)

    def _read_config(self, file_path) -> Dict:
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)

    @property
    def list(self) -> List:
        return self._config['sources']

    @property
    def today(self) -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d")

    @property
    def outputfile(self) -> str:
        return self._config["outputfile"].replace("{date}", self.today)


if __name__ == '__main__':
    config = Config()
    for url in config.list:
        print(url)
