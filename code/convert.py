import yaml
import json
import os

ROOT_DIR = os.getcwd()
CLASH_DIR = f"{ROOT_DIR}/Clash"
SURGE_DIR = f"{ROOT_DIR}/Surge/Rules"
SING_BOX_DIR = f"{ROOT_DIR}/sing-box/source_type"


# 读取YAML文件
def load_yaml(filepath):
    with open(filepath, 'r') as file:
        yaml_data = yaml.safe_load(file)
    return yaml_data


def get_rules_by_type(type, yaml_data):
    payload = yaml_data.get("payload")
    rule_list = []
    for line in payload:
        content = line.split(",")
        if content[0] == type:
            rule_list.append(content[1])
    return rule_list

# 转换为所需的JSON格式
def convert_to_singbox():
    yaml_files = [f[:-5] for f in os.listdir(CLASH_DIR) if f.endswith('.yaml')]
    for name in yaml_files:
        yaml_data = load_yaml(f"{CLASH_DIR}/{name}.yaml")
        json_data = {
            "version": 1,
            "rules": [
                {
                    "domain_suffix": get_rules_by_type("DOMAIN-SUFFIX", yaml_data),
                    "domain": get_rules_by_type("DOMAIN", yaml_data),
                    "domain_keyword": get_rules_by_type("DOMAIN-KEYWORD", yaml_data)
                }
            ]
        }
        # 将转换后的数据写入JSON文件
        with open(f"{SING_BOX_DIR}/{name}.json", 'w') as json_file:
            json.dump(json_data, json_file, indent=2)

def convert_to_surge():
    yaml_files = [f[:-5] for f in os.listdir(CLASH_DIR) if f.endswith('.yaml')]
    for name in yaml_files:
        yaml_data = load_yaml(f"{CLASH_DIR}/{name}.yaml")
        rules = [i + "\n" for i in yaml_data["payload"]]
        with open(f"{SURGE_DIR}/{name}.list", "w") as fp:
            fp.writelines(rules)



def main():
    convert_to_surge()
    convert_to_singbox()

if __name__ == "__main__":
    main()

