import yaml


def read_yaml(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def get_repo_path():
    config = read_yaml(r"./config.yaml")
    return config["root_path"]
