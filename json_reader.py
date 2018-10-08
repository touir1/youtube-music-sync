import json


class JSONReader:

    @staticmethod
    def read_from_file(path):
        data = {}
        with open(path) as f:
            data = json.load(f)
        return data