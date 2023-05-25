"EleutherAI/pythia-70m-deduped"

import yaml

api_key = str()

# Load API key from config.yaml file
with open("config.yaml", "r") as config_file:
    config_data = yaml.safe_load(config_file)
    api_key = config_data["LAMINI"]
    

print(api_key)