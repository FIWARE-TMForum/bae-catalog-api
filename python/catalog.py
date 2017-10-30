import json
import jsonschema
import category

catalog_schema_path = "../jsons/catalogResourceSchema.json"
catalog_example_path = "../jsons/catalogJSONExample.json"
category_schema_path = "../jsons/categoryResourceSchema.json"
category_example_path = "../jsons/catalogJSONExample.json"

category_json_example = json.load(open(category_example_path, 'r'))
catalog_json_example = json.load(open(catalog_example_path, 'r'))
catalog_schema = json.load(open(catalog_schema_path, 'r'))
category_schema = json.load(open(category_schema_path, 'r'))

class Catalog:
    def __init__(self, j, s):
        jsonschema.validate(j, s)
        self.__j = j

    @classmethod
    def build(cls, n, ty, cat, i, href):
        j = {'name': n, 'type': ty, 'category': cat, 'id': i, 'href': href}
        jsonschema.validate(j, catalog_schema)
        return j
        
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
    print(categoryEntity.get_all())
    print(Catalog.build('name','Product Catalog', [categoryEntity.get_all()], '42', 'https://www.github.com'))

if __name__ == "main":
    main()
