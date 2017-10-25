import json
import jsonschema
import category

catalog_schema_path = "/home/samuel/FIWARE/ProductCatalogTest/jsons/catalogResourceSchema.json"
catalog_example_path = "/home/samuel/FIWARE/ProductCatalogTest/catalogJSONExample.json"
category_schema_path = "/home/samuel/FIWARE/ProductCatalogTest/jsons/categoryResourceSchema.json"
category_example_path = "/home/samuel/FIWARE/ProductCatalogTest/categoryJSONExample.json"

category_json_example = json.load(open(category_example_path, 'r'))
catalog_json_example = json.load(open(catalog_example_path, 'r'))
catalog_schema = json.load(open(catalog_schema_path, 'r'))
category_schema = json.load(open(category_schema_path, 'r'))

class Catalog:
    def __init__(self, j, s):
        jsonschema.validate(j, s)
        self.__j = j

    @classmethod
    def build(self, n, ty, cat, rel):
        j = {'name': n, 'type': ty, 'category': cat, 'relatedParty': rel}
        self.__init__(j, category_schema)
        
    def get_data(self, data):
        return self.__j.get(data)
    
    def set_data(self, field, new_data):
        self.__j[field] = new_data

    def to_string(self):
        return "Catalog[<{}>, type={}, category={}, relatedParty={}]".format(self.get_data("name"),
                                                                            self.get_data("type"),
                                                                            self.get_data("category"),
                                                                            self.get_data("relatedParty"))

def main():
    categoryEntity = category.Category(category_json_example, category_schema)
    c = Catalog.build('name','type',categoryEntity.__dict__, 'relatedParty')
    return c

if __name__ == "main":
    main()
