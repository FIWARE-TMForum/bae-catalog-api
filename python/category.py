import json
import jsonschema

category_schema_path = "../jsons/categoryResourceSchema.json"
category_example_path = "../jsons/categoryJSONExample.json"

category_json_example = json.load(open(category_example_path, 'r'))
category_schema = json.load(open(category_schema_path, 'r'))

class Category:
    def __init__(self, j, s):
        jsonschema.validate(j, s)
        self.__j = j

    def is_valid(self):
        return ((self.get_data("isRoot") == "true" and self.get_data("parentId") == "") or
                    (self.get_data("isRoot") == "false" and self.get_data("parentId") != ""))
                    
    def get_data(self, data):
        return self.__j.get(data)
    
    def set_data(self, field, new_data):
        self.__j[field] = new_data
    
    def to_string(self):
        return "Category[<{}>, parentId={}, isRoot={}]".format(self.get_data("name"), self.get_data("parentId"),
                                                               self.get_data("isRoot"))
    def get_all(self):
        return self.__j
