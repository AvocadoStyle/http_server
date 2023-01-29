import json

def get_server_configuration():
    try:
        with open('server_configurations.json', 'r') as config_file:
            return json.load(config_file)
    except:
        print(f"cannot get the data")
        return

def get_file_content(file_name):
    try:
        with open(file_name, "r") as file:
            return file.readlines()
    except:
        print("cannot read file")
        raise Exception("error - can't read file")