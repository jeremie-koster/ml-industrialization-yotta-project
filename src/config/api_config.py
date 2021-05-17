import os
import yaml

# Get API config
ENVIRONMENT = os.getenv("API_CONFIG")
this_dir = os.path.dirname(os.path.realpath(__file__))

if ENVIRONMENT:
    api_config_path = ENVIRONMENT
else:
    api_config_path = os.path.join(this_dir, "api-config.yml")


with open(api_config_path, "r") as api_file:
    api_config = yaml.safe_load(api_file)
