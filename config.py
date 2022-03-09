import yaml

DEFAULT_CONFIG = 'config.yml'

class Config():
    
    def __init__(self, config_file: str = DEFAULT_CONFIG) -> None:
        self._config = self.__read_config(config_file)

    def __read_config(self, file_path) -> dict:    
        with open(file_path, 'r') as f:
            return yaml.safe_load(f)


    @property
    def list(self) -> list:
        return self._config['sources']



if __name__ == '__main__':
    config = Config()
    for url in config.list:
        print (url)



