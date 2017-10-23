import json
import jsonschema
import category

catalog_schema_path = "/home/samuel/FIWARE/ProductCatalogTest/jsons/catalogResourceSchema.json"
json_example_path = "/home/samuel/FIWARE/ProductCatalogTest/catalogJSONExample.json"

json_example = json.load(open(json_example_path, 'r'))
schema = json.load(open(catalog_schema_path, 'r'))

class Catalog:
    def __init__(self, j):
        jsonschema.validate(json_example, schema)
        self.__j = j
                    
    def get_data(self, data):
        return self.__j.get(data)
    
    def set_data(self, field, new_data):
        self.__j[field] = new_data

    def to_string(self):
        return "Catalog[<{}>, type={}, category={}, relatedParty={}]".format(self.get_data("name"),
                                                                            self.get_data("type"),
                                                                            self.get_data("category"),
                                                                            self.get_data("relatedParty"))
