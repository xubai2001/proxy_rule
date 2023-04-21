import yaml
import os


def load_yaml(filename) -> list:
    with open(filename, mode="r") as f:
        content = f.read()
    rules_dict = yaml.safe_load(content)
    return [i + "\n" for i in rules_dict["payload"]]

def write_list(rules: list, filename: str):
    with open(filename, mode="w") as f:
        f.writelines(rules)

def main():
    root_dir = os.getcwd()
    filenames = ["proxy", "direct", "custom_emby", "us", "video", "Bilibili", "chatgpt", "steam"]
    for name in filenames:
        rules = load_yaml(f"{root_dir}/Clash/{name}.yaml")
        write_list(rules, f"{root_dir}/Surge/{name}.list")

if __name__ == "__main__":
    main()
