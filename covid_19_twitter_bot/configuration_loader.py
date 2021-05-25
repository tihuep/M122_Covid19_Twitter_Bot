from pathlib import Path
import yaml
import sys
from configuration import Configuration


def load_configuration(configuration_file):
    configuration_path = Path(configuration_file).absolute()
    if not configuration_path.is_file():
        sys.exit(f"Configuration file '{configuration_path}' does not exist.")
    configuration_string = configuration_path.read_text()
    return Configuration.from_dict(_parse_configuration(configuration_string))


def _parse_configuration(configuration_string):
    return yaml.load(configuration_string, Loader=yaml.FullLoader)
