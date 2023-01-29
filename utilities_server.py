import json
from pathlib import Path
def get_server_configuration():
    try:
        with open('server_configurations.json', 'r') as config_file:
            return json.load(config_file)
    except:
        print(f"cannot get the data")
        return

def get_file_content(file_name):
    try:
        if file_name.endswith('.jpg'):
            kaki = b''
            with open(file_name, "rb") as file:
                kaki = file.read()
                file.close()
                return kaki
        file_name = str(Path(file_name))
        with open(file_name, "r") as file:
            return file.readlines()
    except:
        print("cannot read file")
        raise Exception("error - can't read file")