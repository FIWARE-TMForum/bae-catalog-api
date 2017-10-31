import json
import jsonschema

class Catalog:
    def __init__(self, j, s=None):
        if s:
            jsonschema.validate(j, s)
        self.__j = j

    @classmethod
    def build(cls, n, ty, cat, i, href):
        j = {'name': n, 'type': ty, 'category': cat, 'id': i, 'href': href}
        return Catalog(j)
        
    def get_data(self, data):
        return self.__j.get(data)
    
    def set_data(self, field, new_data):
        self.__j[field] = new_data
