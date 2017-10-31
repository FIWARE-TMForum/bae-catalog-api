import json
import jsonschema

class Category:
    def __init__(self, j, s=None):
        if s:
            jsonschema.validate(j, s)
        self.__j = j

    def is_valid(self):
        return ((self.get_data("isRoot") == "true" and self.get_data("parentId") == "") or
                    (self.get_data("isRoot") == "false" and self.get_data("parentId") != ""))
                    
    def get_data(self, data):
        return self.__j.get(data)
    
    def set_data(self, field, new_data):
        self.__j[field] = new_data
    
    def get_all(self):
        return self.__j
