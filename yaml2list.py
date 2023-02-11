import yaml


def load_yaml(filename) -> list:
    with open(filename, mode="r") as f:
        content = f.read()
    rules_dict = yaml.safe_load(content)
    return [i + "\n" for i in rules_dict["payload"]]

def write_list(rules: list, filename: str):
    with open(filename, mode="w") as f:
        f.writelines(rules)

def main():
    filenames = ["proxy", "direct", "custom_emby", "us", "video"]
    for name in filenames:
        rules = load_yaml(f"{name}.yaml")
        write_list(rules, f"{name}.list")
    print("write complete")

if __name__ == "__main__":
    main()
