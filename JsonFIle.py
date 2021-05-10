import json
import logging


class JsonFile:

    def __init__(self, filepath):
        self.filepath = filepath

    def read_json(self):
        json_file = open(self.filepath, "r")
        data = json.load(json_file)
        json_file.close()
        return data

    def __write_json(self, data):
        json_file = open(self.filepath, "w")
        json.dump(data, json_file)
        json_file.close()

    def update_json(self, update_key, update_value):
        data = self.read_json()
        data[update_key] = update_value
        self.__write_json(data)