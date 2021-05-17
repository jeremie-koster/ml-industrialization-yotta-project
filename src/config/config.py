__all__ = ["config, api_config"]

import os
import yaml

this_dir = os.path.dirname(os.path.realpath(__file__))

# Get data config
config_file_path = os.path.join(this_dir, "config.yml")

with open(config_file_path, "r") as file_in:
    config = yaml.safe_load(file_in)
