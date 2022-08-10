import os

import yaml


class GetData:
    @classmethod
    def load_yaml(cls, path):
        root_path = os.path.relpath(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        )
        yaml_path = os.path.join(root_path, path)
        with open(yaml_path, encoding='utf-8') as f:
            env = yaml.safe_load(f)
            return env
