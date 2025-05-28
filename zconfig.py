import json
import sys


class ZConfig:
    def __init__(self, configname = './config.json'):
        try:
            with open(configname, "r", encoding="utf-8") as f:
                config = json.load(f)
        except Exception as e:
            print(f"open {configname} or load json data failed!")
            sys.exit(-1)
        try:
            self.api_key = config["api_config"]["api_key"]
            self.api_url = config["api_config"]["api_url"]
            self.ai_model = config["api_config"]["model"]
            self.temperature = config["api_config"]["temperature"]
            self.max_tokens = config["api_config"]["max_tokens"]
            self.prompt_file = config["prompt_file"]
            self.log_file = config["log_file"]
        except Exception as e:
            print(f"get config failed!")
            sys.exit(-1)
        finally:
            f.close()
        

