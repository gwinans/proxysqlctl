import os
import yaml


class YAMLConfigHelper:
    def __init__(self):
        self.filename = os.path.expanduser(
            os.path.join("~", ".config", "proxysqlctl", "proxysqlctl.yaml")
        )

    def load(self):
        try:
            with open(self.filename, "r") as f:
                proxysqlctl_yaml = yaml.safe_load(f).get("proxysqlctl")
        except FileNotFoundError:
            return None

        return proxysqlctl_yaml
